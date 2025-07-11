import boto3
import json
import os
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')
table = dynamodb.Table(os.environ.get('TABLE_NAME', 'Resume'))

SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN', 'arn:aws:sns:ap-south-2:358238714507:Resume-SNS')

def lambda_handler(event, context):
    visitor_id = 'main'

    try:
        # Get count from DynamoDB
        response = table.get_item(Key={'id': visitor_id})
        visits = int(response['Item']['visits']) + 1 if 'Item' in response else 1

        # Put new count back
        table.put_item(Item={'id': visitor_id, 'visits': visits})

        # Example condition: alert if visits cross 100
        if visits >= 100:
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject='Resume Site Hit 100+ Visitors',
                Message=f'Your resume site just hit {visits} visitors!'
            )

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'visitorCount': visits})
        }

    except Exception as e:
        # Optional: send error notification
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject='Lambda Error on Resume Site',
            Message=f'Error in Lambda function: {str(e)}'
        )

        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
