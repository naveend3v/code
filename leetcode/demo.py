from datetime import datetime
from dateutil.tz import tzlocal

if a in ['abc','cde']:
a = {
    "Reservations": [
        {
            "ReservationId": "r-062dfd41274b7820a",
            "OwnerId": "271712011597",
            "Groups": [],
            "Instances": [
                {
                    "Architecture": "x86_64",
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/xvda",
                            "Ebs": {
                                "AttachTime": datetime(2026, 2, 8, 6, 26, 23, tzinfo=tzlocal()),
                                "DeleteOnTermination": True,
                                "Status": "attached",
                                "VolumeId": "vol-018c755680bd2a0f4",
                                "EbsCardIndex": 0,
                            },
                        }
                    ],
                    "ClientToken": "42df1a1c-0bb0-4e70-be50-295eac99637a",
                    "EbsOptimized": True,
                    "EnaSupport": True,
                    "Hypervisor": "xen",
                    "NetworkInterfaces": [
                        {
                            "Attachment": {
                                "AttachTime": datetime(2026, 2, 8, 6, 26, 22, tzinfo=tzlocal()),
                                "AttachmentId": "eni-attach-0fcc9453b1be2a78c",
                                "DeleteOnTermination": True,
                                "DeviceIndex": 0,
                                "Status": "attached",
                                "NetworkCardIndex": 0,
                            },
                            "Description": "",
                            "Groups": [
                                {
                                    "GroupId": "sg-05b00f462e2319471",
                                    "GroupName": "launch-wizard-1",
                                }
                            ],
                            "Ipv6Addresses": [],
                            "MacAddress": "0a:ff:e6:38:4a:81",
                            "NetworkInterfaceId": "eni-066495d43a9cba62a",
                            "OwnerId": "271712011597",
                            "PrivateDnsName": "ip-172-31-31-206.ec2.internal",
                            "PrivateIpAddress": "172.31.31.206",
                            "PrivateIpAddresses": [
                                {
                                    "Primary": True,
                                    "PrivateDnsName": "ip-172-31-31-206.ec2.internal",
                                    "PrivateIpAddress": "172.31.31.206",
                                }
                            ],
                            "SourceDestCheck": True,
                            "Status": "in-use",
                            "SubnetId": "subnet-0df8a8450e7971fda",
                            "VpcId": "vpc-0815c1ca63b0c88e7",
                            "InterfaceType": "interface",
                            "Operator": {"Managed": False},
                        }
                    ],
                    "RootDeviceName": "/dev/xvda",
                    "RootDeviceType": "ebs",
                    "SecurityGroups": [
                        {
                            "GroupId": "sg-05b00f462e2319471",
                            "GroupName": "launch-wizard-1",
                        }
                    ],
                    "SourceDestCheck": True,
                    "StateReason": {
                        "Code": "Client.UserInitiatedShutdown",
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown",
                    },
                    "Tags": [{"Key": "Name", "Value": "test1"}],
                    "VirtualizationType": "hvm",
                    "CpuOptions": {"CoreCount": 1, "ThreadsPerCore": 2},
                    "CapacityReservationSpecification": {
                        "CapacityReservationPreference": "open"
                    },
                    "HibernationOptions": {"Configured": False},
                    "MetadataOptions": {
                        "State": "applied",
                        "HttpTokens": "required",
                        "HttpPutResponseHopLimit": 2,
                        "HttpEndpoint": "enabled",
                        "HttpProtocolIpv6": "disabled",
                        "InstanceMetadataTags": "disabled",
                    },
                    "EnclaveOptions": {"Enabled": False},
                    "BootMode": "uefi-preferred",
                    "PlatformDetails": "Linux/UNIX",
                    "UsageOperation": "RunInstances",
                    "UsageOperationUpdateTime": datetime(
                        2026, 2, 8, 6, 26, 22, tzinfo=tzlocal()
                    ),
                    "PrivateDnsNameOptions": {
                        "HostnameType": "ip-name",
                        "EnableResourceNameDnsARecord": True,
                        "EnableResourceNameDnsAAAARecord": False,
                    },
                    "MaintenanceOptions": {
                        "AutoRecovery": "default",
                        "RebootMigration": "default",
                    },
                    "CurrentInstanceBootMode": "uefi",
                    "NetworkPerformanceOptions": {"BandwidthWeighting": "default"},
                    "Operator": {"Managed": False},
                    "InstanceId": "i-0466222f60662e9c5",
                    "ImageId": "ami-0532be01f26a3de55",
                    "State": {"Code": 80, "Name": "stopped"},
                    "PrivateDnsName": "ip-172-31-31-206.ec2.internal",
                    "PublicDnsName": "",
                    "StateTransitionReason": "User initiated (2026-02-08 07:08:49 GMT)",
                    "AmiLaunchIndex": 0,
                    "ProductCodes": [],
                    "InstanceType": "t3.micro",
                    "LaunchTime": datetime(2026, 2, 8, 6, 26, 22, tzinfo=tzlocal()),
                    "Placement": {
                        "AvailabilityZoneId": "use1-az4",
                        "GroupName": "",
                        "Tenancy": "default",
                        "AvailabilityZone": "us-east-1b",
                    },
                    "Monitoring": {"State": "disabled"},
                    "SubnetId": "subnet-0df8a8450e7971fda",
                    "VpcId": "vpc-0815c1ca63b0c88e7",
                    "PrivateIpAddress": "172.31.31.206",
                }
            ],
        }
    ],
    "ResponseMetadata": {
        "RequestId": "9f3a6d95-47cd-447b-aab1-2339a5d05a60",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "9f3a6d95-47cd-447b-aab1-2339a5d05a60",
            "cache-control": "no-cache, no-store",
            "strict-transport-security": "max-age=31536000; includeSubDomains",
            "vary": "accept-encoding",
            "content-type": "text/xml;charset=UTF-8",
            "content-length": "4639",
            "date": "Sun, 08 Feb 2026 14:02:40 GMT",
            "server": "AmazonEC2",
        },
        "RetryAttempts": 0,
    },
}

#print(a["Reservations"][0]['Instances'])

from datetime import datetime
from dateutil.tz import tzlocal

snapshots_data = {
    "Snapshots": [
        {
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "demo1"
                }
            ],
            "StorageTier": "standard",
            "TransferType": "standard",
            "CompletionTime": datetime(
                2026, 2, 8, 6, 27, 43, 817000,
                tzinfo=tzlocal()
            ),
            "FullSnapshotSizeInBytes": 1782054912,
            "SnapshotId": "snap-07c90ac35ef74b22b",
            "VolumeId": "vol-018c755680bd2a0f4",
            "State": "completed",
            "StartTime": datetime(
                2026, 2, 8, 6, 27, 5, 557000,
                tzinfo=tzlocal()
            ),
            "Progress": "100%",
            "OwnerId": "271712011597",
            "Description": "demo-snapshot",
            "VolumeSize": 8,
            "Encrypted": False
        }
    ],
    "ResponseMetadata": {
        "RequestId": "5f98fb33-c6cc-4059-a3db-a4ea8788b7fd",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "5f98fb33-c6cc-4059-a3db-a4ea8788b7fd",
            "cache-control": "no-cache, no-store",
            "strict-transport-security": "max-age=31536000; includeSubDomains",
            "content-type": "text/xml;charset=UTF-8",
            "content-length": "809",
            "date": "Tue, 10 Feb 2026 12:04:22 GMT",
            "server": "AmazonEC2"
        },
        "RetryAttempts": 0
    }
}

