# readcsvfromS3toDynamoDB
This function to read S3 csv object and insert into DynamoDB
Req :
1.Add policy  for IAM role which lambda function maybe need such as : AmazonS3FullAccess, AmazonDynamoDBFullAccess, AWSOpsWorksCloudWatchLogs
2. Create trigger from S3 to PUT file event call lambda function.
3. Create a DynamoDB to storage data.
