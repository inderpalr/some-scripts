# This will be simple logic of boto3 to create an ec2 instance

import boto3
ec2 = boto3.resource('ec2')

def create_ec2():
    ec2.create_instances(ImageId='ami-0915bcb5fa77e4892', MinCount=1, MaxCount=1)


# Stopping the instance
#ids = ['i-00af2ddc6e7965047']
#ec2.instances.filter(InstanceIds=ids).terminate()

# Stopping the instance

def stop_ec2():
  ec2.instances.terminate()
