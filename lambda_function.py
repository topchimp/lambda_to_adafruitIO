import json
import requests

import boto3
import logging
from boto3.dynamodb.conditions import Key

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
urlPM25 =  'https://io.adafruit.com/api/v2/YOUR_ACCOUNT/feeds/pm25/data'
urlPM10 =  'https://io.adafruit.com/api/v2/YOUR_ACCOUNT/feeds/pm10/data'

def post_data(url, my_data):
    myheaders = {'X-AIO-Key': 'YOUR_ADAFRUIT_KEY'}
    response = requests.post(url, data = my_data, headers = myheaders)


def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table = client.Table('pollution_data')
    data_response = table.query(
        KeyConditionExpression = Key('location').eq('XXX'),
        ScanIndexForward = False,
        Limit=1
    )
    temp = data_response['Items']
    the_data25 =  (temp[0]['PM25'])
    myobj25 = {'value': the_data25}
    the_data10 =  (temp[0]['PM10'])
    myobj10 = {'value': the_data10}
    logger.debug('posts data  ' + str(the_data10))

    post_data(urlPM25, myobj25)
    post_data(urlPM10, myobj10)
    return True
