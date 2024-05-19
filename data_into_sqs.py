import requests
import time
import boto3
import os

# Set AWS credentials from environment variables
os.environ['AWS_ACCESS_KEY_ID'] = ''
os.environ['AWS_SECRET_ACCESS_KEY'] = ''
os.environ['AWS_REGION'] = 'us-east-1'

sqs = boto3.client('sqs', region_name=os.environ['AWS_REGION'])
queue_url = 'https://sqs.us-east-1.amazonaws.com/767398136802/Data_collection'


url = "https://latest-stock-price.p.rapidapi.com/any"
headers = {
	"X-RapidAPI-Key": "7e355ebc13mshaf759ddd066491ep15c42cjsn06c191ab7fd1",
	"X-RapidAPI-Host": "latest-stock-price.p.rapidapi.com"
}

def send_message_to_sqs(message):
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message
    )
    print("Message sent to SQS:", response['MessageId'])
    
while True:

	response = requests.get(url, headers=headers)
	Data=response.json()
	send_message_to_sqs(str(Data[0]))
	time.sleep(30)

