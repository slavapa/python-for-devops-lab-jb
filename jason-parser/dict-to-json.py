import json

person_dict = {
    "name": "Slava",
    "age": "51"
}

person_json = json.dumps(person_dict)
print(person_json)

person_json = '{"name":"John"}'

person_dict = json.loads(person_json)
print(person_dict)

create_cluster_result = '''
{
    "cluster": {
        "name": "string",
        "arn": "string",
        "createdAt": "datetime",
        "version": "string",
        "endpoint": "string",
        "roleArn": "string",
        "resourcesVpcConfig": {
            "subnetIds": [
                "string"
            ],
            "securityGroupIds": [
                "string"
            ],
            "clusterSecurityGroupId": "string",
            "vpcId": "string",
            "endpointPublicAccess": "True|False",
            "endpointPrivateAccess": "True|False",
            "publicAccessCidrs": [
                "string"
            ]
        },
        "kubernetesNetworkConfig": {
            "serviceIpv4Cidr": "string",
            "serviceIpv6Cidr": "string",
            "ipFamily": "ipv4"
        },
        "logging": {
            "clusterLogging": [
                {
                    "enabled": "True|False"
                }
            ]
        },
        "identity": {
            "oidc": {
                "issuer": "string"
            }
        },
        "status": "CREATING",
        "certificateAuthority": {
            "data": "string"
        },
        "clientRequestToken": "string",
        "platformVersion": "string",
        "tags": {
            "string": "string"
        },
        "encryptionConfig": [
            {
                "resources": [
                    "string"
                ],
                "provider": {
                    "keyArn": "string"
                }
            }
        ],
        "connectorConfig": {
            "activationId": "string",
            "activationCode": "string",
            "activationExpiry": "datetime",
            "provider": "string",
            "roleArn": "string"
        }
    }
}
'''

create_cluster_dict = json.loads(create_cluster_result)
print(create_cluster_dict)

key_name = "name"
print("The value of the key: {0} is {1}".format(key_name, create_cluster_dict["cluster"][key_name]))

