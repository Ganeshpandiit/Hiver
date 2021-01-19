import boto3
region = "us-west-2"
ec2 = boto3.resource('ec2', region)
instances = ec2.instances.filter(
    Filters=[{'Name': 'vpc-id', 'Values':['vpc-xxxxxxx']}, {'Name': 'instance-type', 'Values':['m5.large']}])
for instance in instances:
    print(instance.id, instance.instance_type)
