import tempfile
from kafka import KafkaProducer

TEMP_DIR = tempfile.mkdtemp()


def producer(message):
    producer = KafkaProducer(
        bootstrap_servers=os.environ["bootstrapServer"],
        security_protocol="SSL",
        ssl_cafile=_download_from_s3("ca.pem"),
        ssl_certfile=_download_from_s3("service.cert"),
        ssl_keyfile=_download_from_s3("service.key"),
    )

    print("Sending: {}".format(message))
    producer.send(os.environ["topic"], message.encode("utf-8"))

    producer.flush()


def _download_from_s3(key):
    """
        Requires a path to a folder. Use when downloading files with directory paths.
    """
    s3 = boto3.client('s3')
    logging.info('Downloading file from s3: %s', key)
    s3.download_file(os.environ['certsKeysBucket'], key, TEMP_DIR + '/{}'.format(str(key)))
    return TEMP_DIR + '/{}'.format(str(key))
