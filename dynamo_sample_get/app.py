import json
import os
import boto3


def lambda_handler(event, context):
    user_table_name = os.environ['USER_TABLE']
    _username = event['queryStringParameters']['username']
    dynamodb = boto3.resource('dynamodb')
    users = dynamodb.Table(user_table_name)
    response = users.get_item(Key={
        'username': _username
    })

    return {
        'statusCode': 200,
        'body': json.dumps(response['Item'])
    }
