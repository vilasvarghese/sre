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
    ami-0a84ffe13366e143f - my k8s ami in ngv before init 
    ami-0866a3c8686eaeeba - ubuntu in nvg
    ami-00123da0a7af05c8b - antariksha ami 
    """
    try:
        print ("Creating EC2 instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId="ami-0a84ffe13366e143f",
            MinCount=2,
            MaxCount=2,
            InstanceType="t2.large",
            KeyName="anubhavnv"
            #["richardnv", "mittanv", "amithnv", "willchristnv", "minnunv", "sheethalnv", "ashwanthramnv", "doddegowdanv", 
            #"gunjannv", "samitnv", "akshatnv", "tusharnv", "ayushnv", "anubhavnv"]
        )
    except Exception as e:
        print(e)
            
            
            
            #https://267092042432.signin.aws.amazon.com/console

def create_ec2_spot_instance(key):
    """
    MaxCount=1, # Keep the max count to 1, unless you have a requirement to increase it
    InstanceType="t2.micro", # Change it as per your need, But use the Free tier one
    KeyName="ec2-key" # Change it to the name of the key you have.
    :return: Creates the EC2 instance.
    
    Amazon ami: ami-079db87dc4c10ac91 in nvg
    Centos ami: ami-05a36e1502605b4aa
    Ubuntu ami: ami-0c7217cdde317cfec in ngv
    Ununtu ami in us-west-2: ami-0cf2b4e024cdb6960
    my k8s ami - ami-0a84ffe13366e143f
    """
    try:
        print ("Creating EC2 instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.request_spot_instances(
            LaunchSpecification={
                'ImageId': "ami-04f59c565deeb2199",#"ami-0521bc4c70257a054",#"ami-0521bc4c70257a054",#rhel mum #ubuntu mumbai "ami-033a03819e5147e3f", #'ami-0a84ffe13366e143f'-k8s,#'ami-0b05d988257befbbe', - ohio, ami-020cba7c55df1f615 -nv  
                'KeyName': key,
                'InstanceType': 't2.large',
            'Placement': {
                'AvailabilityZone': 'us-east-1a',
            }
        }
        )
    except Exception as e:
        print(e)

    

def create_multiple_instances():
  """
  This function takes an array as input and loops through it,
  calling the 'print_value' function for each element.
  """
  #Richard, Yashwanth Mitta, Amith, Minnu, Sheethal, Ashwanthram, Yaswanth Doddegowda, Gunjan, Samit, Akshat 
  #Tushar, Ayush, Anubhav 
  #data_array = ["Gunjan","Doddegowda","Samit", "Minnu", "Sheethal", "Mitta", "Anubhav"]
  #data_array = ["richardnv", "mittanv", "amithnv", "willchristnv", "minnunv", "sheethalnv", "ashwanthramnv", "doddegowdanv", "gunjannv", "samitnv", "akshatnv", "tusharnv", "ayushnv", "anubhavnv"]
  data_array = ["richardnv", "mittanv", "amithnv", "willchristnv", "minnunv", "sheethalnv", "ashwanthramnv", "doddegowdanv", "gunjannv", "samitnv", "akshatnv", "tusharnv", "ayushnv", "anubhavnv"]
  
 
  #["Richard", "Mitta", "Amith", "WillChrist", "Minnu", "Sheethal", "Ashwanthram", "Doddegowda", "Gunjan", "Samit", "Akshat", "Tushar", "Ayush", "Anubhav"]
  
  #data_array = ["prabhath","anusha","sruthi","satish","lohitha","nutan","satwika","mohana","rithvik","pratham","preethi", "vivek", "kavya", "harsha", "sujith", "harshitha", "bhavya", "geethika", "sanjana", "harsha2", "indu"]#"indu",
  #data_array = ["indu"]
  for item in data_array:
    create_ec2_spot_instance(item)




def create_ec2_spot_instance_withHarkDisk():
    """
    MaxCount=1, # Keep the max count to 1, unless you have a requirement to increase it
    InstanceType="t2.micro", # Change it as per your need, But use the Free tier one
    KeyName="ec2-key" # Change it to the name of the key you have.
    :return: Creates the EC2 instance.
    
    Amazon ami: ami-079db87dc4c10ac91 in nvg
    Centos ami: ami-05a36e1502605b4aa
    Ubuntu ami: ami-0c7217cdde317cfec in ngv
    Ununtu ami in us-west-2: ami-0cf2b4e024cdb6960
    """
    try:
    
        print("Creating EC2 instance")
        resource_ec2 = boto3.client("ec2")
        
        dev_sda1 = resource_ec2.blockdevicemapping.EBSBlockDeviceType()
        dev_sda1.size = 50 # size in Gigabytes
        bdm = resource_ec2.blockdevicemapping.BlockDeviceMapping()
        bdm['/dev/sda1'] = dev_sda1 
        
        
        resource_ec2.request_spot_instances(
            LaunchSpecification={
                'ImageId': 'ami-0ebfd941bbafe70c6',
                'KeyName': 'cgi',
                'InstanceType': 't2.micro',
                'block_device_mappings': '[bdm]',
                'Placement': {
                    'AvailabilityZone': 'us-east-1a',
                }
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
    #     "Public IP: {0}, Key: {1}\n".format(
    #     instance.public_ip_address, instance.key.name
    #     )
    # )
     #
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



#import json
#import boto3

def list_stopped_instance():
    ec2_client = boto3.client("ec2", region_name="us-east-1")

    instances = ec2_client.describe_instances(
        Filters=[
            { "Name": "tag:Name", "Values": ["Vilas"] },
            { "Name": "instance-state-name", "Values": ["stopped"] }
        ]
    )

    for reservation in instances["Reservations"]:
        for instance in reservation["Instances"]:
            #print(instance['InstanceId'])
            ec2.instances.filter(InstanceIds=instance['InstanceId']).start()
       


def start_all_instances_client():
   ec2 = boto3.client('ec2', region_name='us-east-1')
   instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']},{'Name': 'tag:auto-start-stop','Values':['Yes']}])
   for instance in instances:
       id=instance.id
       ec2.instances.filter(InstanceIds=[id]).stop()
       print("Instance ID is stopped:- "+instance.id)
   return "success"
   

def stop_all_instances():
    try: 
        ec2 = boto3.resource('ec2')
        instances = ec2.instances.filter(Filters=[{'Values': ['running']}])
        instance_ids = [instance.id for instance in instances]
        ec2.instances.filter(InstanceIds=instance_ids).stop()
    except Exception as e:
        print(e)
        
def start_all_instances():
    try: 
        ec2 = boto3.resource('ec2')
        
        #instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name','Values': ['stopped']}])
        instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
        
        print (ec2)
        #filters = [{'Name': 'instance-state-name', 'Values': ['Stopped']}]
        #instances = ec2.instances.filter(Filters=[{'Values': ['stopped']}])
        #instances = ec2.instances.filter(Filters=filters)
        print (instances)
        instance_ids = [instance.id for instance in instances]
        print (instance_ids)
        ec2.instances.filter(InstanceIds=instance_ids).start()
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
 
#create_ec2_spot_instance_withHarkDisk() 
#create_ec2_instance()
#get_all_instances_public_ip()
#create_ec2_spot_instance('vilasnv')
create_multiple_instances()
#print_all_instances()
#describe_ec2_instance()
#reboot_ec2_instance()
#stop_ec2_instance()
#start_ec2_instance()
#terminate_ec2_instance()