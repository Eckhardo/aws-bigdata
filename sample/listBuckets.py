import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
# for bucket in s3.buckets.all():
#   print(bucket.name)

bucket_name='my-rusken-orderlogs'
orderlogsBucket = s3.Bucket(bucket_name)
print('My Glue Bucket: {}' .format(orderlogsBucket.name))


print('My Glue Buckets Objects: {}' .format(orderlogsBucket.objects.all()))
 
response = s3.Bucket(bucket_name).objects.all()
print('My Glue Buckets Response: {}' .format(response))


for item in response:
   print('key: {} {}' .format(item.key, item.last_modified))


