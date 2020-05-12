import json
import logging
import os

import boto3

logger = logging.getLogger()


def lambda_handler(event, context):
    user_table_name = os.environ['USER_TABLE']
    new_user = json.loads(event['body'])
    dynamodb = boto3.resource('dynamodb')
    users = dynamodb.Table(user_table_name)
    response = users.put_item(Item=new_user)
    logger.info(response)
    return {
        'statusCode': 200
    }
