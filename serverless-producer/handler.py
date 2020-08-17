import json
import logging
from producer import producer
from monitor import monitor

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler():
    """
        Monitor a website and upload analytics to a database.
    """
    website_response = monitor()
    producer(website_response)

    response = create_http_response(200, "Success!")

    return response
    

def create_http_response(statuscode, body):

    response = {
        "statusCode": statuscode,
        "body": json.dumps(body)
    }

    return response
