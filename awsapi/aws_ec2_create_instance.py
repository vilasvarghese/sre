# Lets create EC2 instances using Python BOTO3
import boto3


def create_ec2_instance():
    """
    MaxCount=1, # Keep the max count to 1, unless you have a requirement to increase it
    InstanceType="t2.micro", # Change it as per your need, But use the Free tier one
    KeyName="ec2-key" # Change it to the name of the key you have.
    :return: Creates the EC2 instance.
    
    Amazon ami: ami-079db87dc4c10ac91 in nvg
    Centos ami: ami-05a36e1502605b4aa
    Ubuntu ami: ami-0c7217cdde317cfec in ngv
    """
    try:
        print ("Creating EC2 instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId="ami-06aa3f7caf3a30282",
            MinCount=2,
            MaxCount=2,
            InstanceType="t3.medium",
            KeyName="shishir"
        )
    except Exception as e:
        print(e)
#subro, purvi, sayantan, monalisa, darshan, rahul, william, sayan, mohinder, jyotishman, sankalita, utkarsh, poorna, uday, shishir

def create_ec2_spot_instance():
    """
    MaxCount=1, # Keep the max count to 1, unless you have a requirement to increase it
    InstanceType="t2.micro", # Change it as per your need, But use the Free tier one
    KeyName="ec2-key" # Change it to the name of the key you have.
    :return: Creates the EC2 instance.
    
    Amazon ami: ami-079db87dc4c10ac91 in nvg
    Centos ami: ami-05a36e1502605b4aa
    Ubuntu ami: ami-0c7217cdde317cfec in ngv
    """
    try:
        print ("Creating EC2 instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.request_spot_instances(
            LaunchSpecification={
                'ImageId': 'ami-0e9107ed11be76fde',
                'KeyName': 'shishir',
                'InstanceType': 't3a.medium',
            'Placement': {
                'AvailabilityZone': 'us-east-1a',
            }

            #subro, purvi, sayantan, monalisa, darshan, rahul, william, sayan, mohinder, jyotishman, sankalita, utkarsh, poorna
        }
        )
    except Exception as e:
        print(e)
    


def describe_ec2_instance():
    try:
        print ("Describing EC2 instance")
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
        return str(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
    except Exception as e:
        print(e)




def get_all_instances_public_ip():
 ec2 = boto3.resource('ec2')
 running_instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

 for instance in running_instances.all():
     #print(
     #    "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
     #    instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
     #    )
     #)
     instance_name = [tag['Value'] for tag in instance.tags if tag['Key'] == 'Name'][0]
     print(
         "Name: {0}, Public IP: {1}\n".format(
         instance_name, instance.public_ip_address
         )
     )





def print_all_instances():
    # Create an EC2 client
    ec2_client = boto3.client('ec2')

    # Filter for running instances
    filters = [{'Name': 'instance-state-name', 'Values': ['running']}]

    # Describe all running instances
    response = ec2_client.describe_instances(Filters=filters)

    # Iterate through instances and print their public IP addresses
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            public_ip_address = instance.get('PublicIpAddress')
            if public_ip_address:
                print("Instance ID:", instance['InstanceId'])
                print("Public IP address:", public_ip_address)
                print("-----------------------")



def reboot_ec2_instance():
    try:
        print ("Reboot EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.reboot_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)


def stop_ec2_instance():
    try:
        print ("Stop EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.stop_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)


def start_ec2_instance():
    try:
        print ("Start EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.start_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)


def terminate_ec2_instance():
    try:
        print ("Terminate EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.terminate_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)

get_all_instances_public_ip()
#create_ec2_spot_instance()
#create_ec2_spot_instance()
#print_all_instances()
#create_ec2_instance()
#describe_ec2_instance()
#reboot_ec2_instance()
#stop_ec2_instance()
#start_ec2_instance()
#terminate_ec2_instance()