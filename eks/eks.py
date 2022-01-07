import boto3

class Eks:
    def __init__(self):
        self.clinet = boto3.client("eks")
        self.region = "us-east-1"


    def create_eks(self, name, roleArn, resourcesVpcConfig ):
        result = self.clinet.create_cluster(name, roleArn, resourcesVpcConfig)
        return result

