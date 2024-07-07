import boto3

# Create an IAM client
iam = boto3.client('iam')

# Function to list users (handles pagination)
def list_all_users():
    paginator = iam.get_paginator('list_users')
    
    for page in paginator.paginate():
        for user in page['Users']:
            print(user['UserName'])




#iam = boto3.client('iam')

def create_user():
    # Create a user
    response = iam.create_user(UserName='new_user')

    # Create a group
    response = iam.create_group(GroupName='developers')

    # Add user to group
    response = iam.add_user_to_group(
        GroupName='developers',
        UserName='new_user'
    )

create_user()
# Call the function to list users
list_all_users()

'''
Import Boto3:  We start by importing the Boto3 library.

Create IAM Client: We create an IAM client object (iam). This object will be used to interact with the IAM service.

list_all_users Function:

Paginator: We use the get_paginator method to create a paginator for the list_users operation. Paginators are essential when you have a potentially large number of users, as they automatically handle fetching users in batches (pages).
Iteration: The code iterates over the paginated results. For each page, it iterates over the Users list within the page, printing each user's UserName.
Function Call: The list_all_users() function is called to initiate the listing process.

Additional Notes:

Error Handling: Consider adding try...except blocks to handle potential AWS service errors gracefully.
Filtering: If you want to filter users by a specific path prefix, use the PathPrefix parameter in the paginate method:
'''