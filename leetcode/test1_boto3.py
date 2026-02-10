import boto3

ec2_client = boto3.client('ec2')
active_ec2_instances = []
ebs_snapshots = []

def getInstances():
    response = ec2_client.describe_instances()
    try:
        if(response['ResponseMetadata']['HTTPStatusCode']!=200):
            print("Connection Failed!!")
        else:
            for i in range(len(response["Reservations"][0]['Instances'])):
                print(response["Reservations"][0]['Instances'][i]['State'])
                if(response["Reservations"][0]['Instances'][i]['State']['Name'] in ['running','stopped']):
                    temp_dict = {
                        'instance_id' : response["Reservations"][0]['Instances'][i]['InstanceId'],
                        'Status' : response["Reservations"][0]['Instances'][i]['State']['Name'],
                        'ebs_volume': response["Reservations"][0]['Instances'][i]['BlockDeviceMappings'][0]['Ebs']['VolumeId']
                    }
                    active_ec2_instances.append(temp_dict)
            print('Active Instances:')
            for i in range(len(active_ec2_instances)):
                print(active_ec2_instances[i])

    except:
        print("Error found")

getInstances()

ebs_client = boto3.client('ec2')

def getSnapShots():
    response = ebs_client.describe_snapshots(OwnerIds=['self'])
    print(response)

getSnapShots()