import json
import logging
import secrets
from consumer import consumer
from database import  write_to_db

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def main():
    """
        Monitor a website and upload analytics to a database.
    """
    message_value = consumer()
    logger.info(message_value)
    message_value = _byte_to_dict()
    message_value["id"] = secrets.randbelow(15)
    write_to_db(message_value)

    return create_http_response(statuscode, body)
    

def _byte_to_dict(message_value):
    message_value = message_value.decode('utf-8')
    message_value = json.loads(message_value)
    headers = message_value["headers"]
    headers = json.loads(headers)
    del message_value["headers"]
    message_value = {**headers, **message_value}

    return message_value


def create_http_response(statuscode, body):

    response = {
        "statusCode": statuscode,
        "body": json.dumps(body)
    }

    return response
