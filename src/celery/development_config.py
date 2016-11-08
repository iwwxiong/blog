# -*-coding: utf-8 -*-
# celery config for development.

# Broken地址
BROKER_URL = 'amqp://wwxiong:Foxconn123@192.168.33.10:5672/wwxhost'

# backend
CELERY_RESULT_BACKEND = 'amqp://wwxiong:Foxconn123@192.168.33.10:5672/wwxhost'