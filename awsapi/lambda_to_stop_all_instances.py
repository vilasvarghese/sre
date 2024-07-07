import json
import boto3

def lambda_handler(event, context):
    
    try:
        # Use the EC2 client for stop_instances
        ec2_client = boto3.client('ec2')

        # Describe running instances (no need to filter twice)
        response = ec2_client.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
        )

        # Extract instance IDs
        instance_ids = [
            instance['InstanceId'] 
            for reservation in response['Reservations']
            for instance in reservation['Instances']
        ]

        # Stop the instances
        if instance_ids:  # Check if any instances were found
            ec2_client.stop_instances(InstanceIds=instance_ids)
        else:
            print("No running instances found to stop.")

        return {
            'statusCode': 200,
            'body': json.dumps('Instances stopped successfully!')  
        }

    except Exception as e:
        print(f"Error stopping instances: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error stopping instances')
        }

#When you execute above code. It may timeout in 3 seconds. Please increase the timeout to 15 seconds. 
#Go to configuration -> Generatl Configuration - Edit Timeout