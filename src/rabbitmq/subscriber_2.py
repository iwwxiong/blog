# -*-coding: utf-8 -*-

"""
client for subscriber 2 with routing_key 'wwxiong.subscriber_2'
"""

import amqp


def _callback(msg):
    """
    消息接收回调函数
    """
    print 'Subscriber_2 received: ' + msg.body


if __name__ == '__main__':
    conn = amqp.Connection(
        host='127.0.0.1',
        userid='wwxiong',
        password='wwxiong',
        virtual_host='wwxhost'
    )
    channel = conn.channel()
    channel.queue_declare(queue='test_queue_2', durable=True, auto_delete=False, exclusive=False)
    channel.queue_bind(queue='test_queue_2', exchange='test_exchange', routing_key='wwxiong.*')
    channel.basic_consume(
        queue='test_queue_2',
        no_ack=True, 
        callback=_callback, 
        consumer_tag='subscriber_2'
    )
    while 1:
        channel.wait()
