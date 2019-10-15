import json
import boto3
import time

def lambda_handler(event, context):
    key = "data.json"
    s3 = boto3.resource('s3')
    storeData = {}
    storeData['data1'] = event['data1']
    storeData['data2'] = event['data2']
    storeData['data3'] = event['data3']
    storeData['average'] = (event['data1'] + event['data2'] + event['data3'])/3
    jsonData = json.dumps(storeData)
    s3.Bucket('lambdatestdata').put_object(Key=key, Body = jsonData)
    return
    #raise Exception('Something went wrong')                
