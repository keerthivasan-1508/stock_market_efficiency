import json
import boto3
from decimal import Decimal
from datetime import datetime

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('StockData')

def lambda_handler(event, context):
    print('===>1')
    print(event)
    for record in event['Records']:
        print('===>2')
        print(record)
        stock_data = json.loads(record['body'].replace("'", '"'))
        print('===>3')
        print(stock_data)
        stock_price = Decimal(str(stock_data['lastPrice']))
        high = Decimal(str(stock_data['dayHigh']))
        low = Decimal(str(stock_data['dayLow']))
        timestamp = datetime.now().isoformat()  # Get current timestamp

        table.put_item(
            Item={
                'Time': timestamp,  # Add the current timestamp
                'stock_price': stock_price,
                'high': high,
                'low': low
            }
        )
    return {
        'statusCode': 200,
        'body': json.dumps('Data inserted into DynamoDB successfully!')
    }
