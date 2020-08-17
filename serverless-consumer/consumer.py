from kafka import KafkaConsumer


def consumer():
    consumer = KafkaConsumer(
        "kafka-monitoring",
        auto_offset_reset=os.environ["servers"],
        client_id=os.environ["clientId"],
        group_id=os.environ["groupId"],
        security_protocol="SSL",
        ssl_cafile=_download_from_s3("ca.pem"),
        ssl_certfile=_download_from_s3("service.cert"),
        ssl_keyfile=_download_from_s3("service.key"),
    )

    raw_msgs = consumer.poll(timeout_ms=1000)
    for tp, msgs in raw_msgs.items():
        for msg in msgs:
            print("Received: {}".format(msg.value))
            return msg.value

    consumer.commit()


def _download_from_s3(key):
    """
        Requires a path to a folder. Use when downloading files with directory paths.
    """
    s3 = boto3.client('s3')
    logging.info('Downloading file from s3: %s', key)
    s3.download_file(os.environ['certsKeysBucket'], key, TEMP_DIR + '/{}'.format(str(key)))
    return TEMP_DIR + '/{}'.format(str(key))
