import boto3
import csv
from urllib.parse import unquote_plus


s3=boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
region='ap-northeast-1'
tablename='day4-dynamodb'
print('Start processing')
def lambda_handler(event, context):
    recList=[]
    try:            
        'get bucketname from event'
        bucketname = event['Records'][0]['s3']['bucket']['name']
        'get bucketkey from event'
        bucketkey = unquote_plus(event['Records'][0]['s3']['object']['key'])
        confile= s3.get_object(Bucket=bucketname, Key=bucketkey)
        'read file with utf-8 encode'
        recList = confile['Body'].read().decode('utf-8').split('\n')

        firstrecord=True
        csv_reader = csv.reader(recList, delimiter=',', quotechar='"')
        'get lenght of list , not include first record'
        lenght = len(recList)
        i = 0
        for row in csv_reader:
            'not refer first record'
            if (firstrecord):
                firstrecord=False
                i = i + 1
                continue
            'start from second record'
            if i <= lenght - 1:
                city = row[0]
                name = row[1]
                age = row[2]
                date = row[3]
                table = dynamodb.Table(tablename)
                response = table.put_item(
                    Item={
                    'city' : city,
                    'name': name,
                    'age': age,
                    'date': date
                    }
                )
                i = i + 1
        print('Put succeeded:')
        print('End processing')
    except Exception as e:
        print (str(e))
