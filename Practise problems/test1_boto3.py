import boto3

ec2_client = boto3.client('ec2')

# def getInstances():
#     response = ec2_client.describe_instances()
#     active_ec2_instances = []
#     try:
#         if(response['ResponseMetadata']['HTTPStatusCode']!=200):
#             print("Connection Failed!!")
#         else:
#             for i in range(len(response["Reservations"][0]['Instances'])):
#                 print(response["Reservations"][0]['Instances'][i]['State'])
#                 if(response["Reservations"][0]['Instances'][i]['State']['Name']=='running'):
#                     active_ec2_instances.append(response["Reservations"][0]['Instances'][i]['InstanceId'])
#             print('Active Instances:')
#             for i in range(len(active_ec2_instances)):
#                 print(f'- {active_ec2_instances[i]}')

#     except:
#         print("Error found")

# getInstances()

ebs_client = boto3.client('ec2')

def getSnapShots():
    response = ebs_client.describe_snapshots()
    print(response)

getSnapShots()