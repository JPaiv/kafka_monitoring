import requests
import logging
import time
import json
import boto3
import os
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

BUCKETNAME = os.environ["contentTextBucket"]


def monitor():
    """
        Get website metrics like response time, response status code. Upload important metrics to database and upload content text to s3.
    """
    url = "http://kydi.fi/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    start = time.time()
    response = requests.get(url, headers=headers)
    end = time.time()
    response_time = end - start

    response_parsed_data = {}
    response_parsed_data["headers"] = json.dumps(dict(response.headers))
    response_parsed_data["status_code"] = response.status_code
    response_parsed_data["response_time"] = response_time
    response_parsed_data["response_text"] = response.text
    response_text = response_parsed_data["response_text"]
    _save_content_text_to_s3(response_text)
    del response_parsed_data["response_text"]
    response_parsed_data = json.dumps(response_parsed_data)

    logger.info(response_parsed_data)
    logger.info(type(response_parsed_data))

    return response_parsed_data


def _save_content_text_to_s3(response_text):
    s3 = boto3.resource(
        's3',
        region_name='eu-central-1'
    )
    object_time = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    s3.Object(BUCKETNAME, f'{object_time}.json').put(Body=response_text)
