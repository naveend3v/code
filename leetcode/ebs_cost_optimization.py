import boto3

client = boto3.client('ec2')

def find_stale_snapshots():
    # get all snapshots owned by the user.
    ebs_snapshots = client.describe_snapshots(OwnerIds=['self'])
    print(f'Total Snapshots: {len(ebs_snapshots["Snapshots"])} \n{[snapshot['SnapshotId'] for snapshot in ebs_snapshots['Snapshots']]}')

    # get all active ec2 instances
    ec2_instances_response = client.describe_instances(Filters=[{'Name':'instance-state-name','Values':['running']}])
    active_ec2_instances = set()

    # adding all active ec2 instances id's
    for reservation in ec2_instances_response['Reservations']:
        for instance in reservation['Instances']:
            active_ec2_instances.add(instance['InstanceId'])
    print(f'Total Active EC2 Instances: {len(active_ec2_instances)} \n{active_ec2_instances}')

    # find stale snapshots not used by any active ec2 instance and not associated with any ebs volume
    for snapshot in ebs_snapshots['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot['VolumeId']
        
        # delete snapshot which is not attached to any volume    
        if not volume_id:
            client.delete_snapshot(SnapshotId = snapshot_id)
            print(f'Deleted Snapshot with "{snapshot_id}" where VolumeId is empty.')
        
        # delete snapshot where the volume is not attached to any active ec2 instance
        try:
            volume_response = client.describe_volumes(VolumeIds = [volume_id])

            if not volume_response['Volumes'][0]['Attachments']:
                client.delete_snapshot(SnapshotId = snapshot_id)
                print(f'Deleted Snapshot with "{snapshot_id}" where VolumeId "{volume_id}" is not attached to any EC2 instance.')

        except client.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    # The volume associated with the snapshot is not found (it might have been deleted)
                    client.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")


find_stale_snapshots()