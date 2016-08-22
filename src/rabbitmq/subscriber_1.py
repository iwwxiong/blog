# -*-coding: utf-8 -*-

"""
client for subscriber 1 with routing_key 'wwxiong.subscriber_1'
"""

import amqp


def _callback(msg):
    """
    消息接收回调函数
    """
    print u'Subscriber_1 received: ' + msg.body


if __name__ == '__main__':
    conn = amqp.Connection(
        host='127.0.0.1',
        userid='wwxiong',
        password='wwxiong',
        virtual_host='wwxhost'
    )
    channel = conn.channel()
    channel.queue_declare(queue='test_queue_1', durable=True, auto_delete=False, exclusive=False)
    channel.queue_bind(queue='test_queue_1', exchange='test_exchange', routing_key='wwxiong.#')
    channel.basic_consume(
        queue='test_queue_1',
        no_ack=True, 
        callback=_callback, 
        consumer_tag='subscriber_1'
    )
    while 1:
        channel.wait()
