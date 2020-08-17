from kafka import KafkaProducer


def producer(message):
    producer = KafkaProducer(
        bootstrap_servers="kafka-e997cda-paivarinta-ac3e.aivencloud.com:29903",
        security_protocol="SSL",
        ssl_cafile="ca.pem",
        ssl_certfile="service.cert",
        ssl_keyfile="service.key",
    )

    print("Sending: {}".format(message))
    producer.send("kafka-monitoring", message.encode("utf-8"))

    producer.flush()
