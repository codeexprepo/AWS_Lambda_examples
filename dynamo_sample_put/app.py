import json
import logging

import boto3
from requests import Request

logger = logging.getLogger()


def lambda_handler(event, context):
    new_user = json.loads(event['body'])
    dynamodb = boto3.resource('dynamodb')
    users = dynamodb.Table('Users')
    response = users.put_item(Item=new_user)
    logger.info(response)
    return {
        'statusCode': 200
    }
