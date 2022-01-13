import boto3
import uuid

access_key = "AKIAXLEKZJVVUKDMBU7X"
secret_key = "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"
region = "eu-west-2"

# client = boto3.client('s3')
client = boto3.client('s3',
                      aws_access_key_id=access_key,
                      aws_secret_access_key=secret_key, region_name=region)

s3_resource = boto3.resource('s3',
                             aws_access_key_id=access_key,
                             aws_secret_access_key=secret_key, region_name=region)


# s3 = boto3.resource('s3')
# bucket = s3.Bucket('name')

def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])


def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name, bucket_response


# first_bucket_name, first_response = create_bucket("slavap13", s3_resource)
# print(first_response)

# second_bucket_name, second_response = create_bucket("slavap13", client)
# print(second_response)

# YOUR_BUCKET_NAME = create_bucket_name("slava13")
# s3_resource.create_bucket(Bucket=YOUR_BUCKET_NAME,
#                           CreateBucketConfiguration={
#                               'LocationConstraint': region})


def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, 'w') as f:
        f.write(str(file_content) * size)
    return random_file_name


# response = client.get_object(
#     Bucket='examplebucket',
#     Key='HappyFace.jpg',
# )
#
# print(response)

response = client.list_buckets()

first_bucket_name = "slavap13cae02715-80dd-4b0e-9a2b-819382ce5d97"
second_bucket_name = "slavap137ab936a4-587d-4d55-88b1-3e9b7bed9460"
# first_file_name = create_temp_file(300, 'firstfile.txt', 'f')

first_file_name = "5e1ec8firstfile_1.txt"
second_file_name = "c1db56firstfile_2.txt"
third_file_name = "ef969efirstfile_3.txt"
third_4_file_name = "ba4611firstfile_4.txt"

first_bucket = s3_resource.Bucket(name=first_bucket_name)
print(f"first_bucket {first_bucket}")
first_object = s3_resource.Object(
    bucket_name=first_bucket_name, key=first_file_name)
print(f"first_object {first_object}")

# first_object_again = first_object.Object(first_file_name)
# print(f"first_object_again {first_object_again}")
first_bucket_again = first_object.Bucket()
print(f"first_bucket_again {first_bucket_again}")

s3_resource.Object(first_bucket_name, first_file_name).upload_file(
    Filename=first_file_name)

first_object.upload_file(second_file_name)

s3_resource.Bucket(first_bucket_name).upload_file(
    Filename=third_file_name, Key=third_file_name)

s3_resource.meta.client.upload_file(
    Filename=third_4_file_name, Bucket=first_bucket_name,
    Key=third_4_file_name)

random_file_name = ''.join([str(uuid.uuid4().hex[:6]), first_file_name])

tmpFileName = f"./tmp/{random_file_name}"
s3_resource.Object(first_bucket_name, first_file_name).download_file(tmpFileName)
print(f"The filename downloaded successfully: {random_file_name}")


def copy_to_bucket(bucket_from_name, bucket_to_name, file_name):
    copy_source = {
        'Bucket': bucket_from_name,
        'Key': file_name
    }
    s3_resource.Object(bucket_to_name, file_name).copy(copy_source)


copy_to_bucket(first_bucket_name, second_bucket_name, first_file_name)

s3_resource.Object(second_bucket_name, first_file_name).delete()

obj = s3_resource.Object(bucket_name=first_bucket_name, key=third_4_file_name)
obj.delete()
print(f"The third_4_file_name filename deleted successfully: {third_4_file_name}")
# s3_resource.Object(first_bucket_name, first_file_name).delete()
# print(f"The second_file_name filename deleted successfully: {first_bucket_name}")
# s3_resource.Object(first_bucket_name, second_file_name).delete()
# print(f"The second_file_name filename deleted successfully: {second_file_name}")
# s3_resource.Object(first_bucket_name, "c1db56firstfile.txt").delete()
# print(f"The second_file_name filename deleted successfully: c1db56firstfile")
# s3_resource.Object(first_bucket_name, third_file_name).delete()
# print(f"The third_file_name filename deleted successfully: {third_file_name}")
# s3_resource.Object(first_bucket_name, "not_existing_file.txt").delete()
