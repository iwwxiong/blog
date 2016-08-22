# -*-coding: utf-8 -*-

import os
import amqp

HOST = '127.0.0.1'
USERID = 'wwxiong'
PASSWORD = 'wwxiong'
VIRTUAL_HOST = 'wwxhost'


def connect(host, userid, password, virtual_host):
    """
    连接amqp服务器
    """
    return amqp.Connection(host=host, userid=userid, password=password, virtual_host=virtual_host)


def create_message(body, **properties):
    """
    创建消息
    """
    msg = amqp.Message(body)
    for key, value in properties.items():
        msg.properties[key] = value
    return msg


def publish_message(channel, msg, exchange, routing_key):
    if not isinstance(msg, amqp.Message):
        raise(u'Param msg must be intance of amqp.Message.')
    return channel.basic_publish(msg, exchange=exchange, routing_key=routing_key)


if __name__ == '__main__':
    conn = connect(HOST, USERID, PASSWORD, VIRTUAL_HOST)
    publish_channel = conn.channel()
    publish_channel.exchange_declare(exchange='test_exchange', type='topic', durable=True, auto_delete=False)
    while 1:
        routing_key, body = raw_input('Please input routing_key and message split with &:').split('&')
        if body == 'exit':
            publish_channel.close()
            conn.close()
            os._exit(0)
        publish_message(conn.channel(), create_message(body, delevery_mode=2), exchange='test_exchange', routing_key=routing_key)