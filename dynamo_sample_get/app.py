import json

import boto3


def lambda_handler(event, context):
    _username = event['queryStringParameters']['username']
    dynamodb = boto3.resource('dynamodb')
    users = dynamodb.Table('Users')
    response = users.get_item(Key={
        'username': _username
    })

    return {
        'statusCode': 200,
        'body': json.dumps(response['Item'])
    }
