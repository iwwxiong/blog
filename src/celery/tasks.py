# -*-coding: utf-8 -*-

import celery

broker = 'amqp://wwxiong:Foxconn123@192.168.33.10:5672/wwxhost'
backend = 'amqp://wwxiong:Foxconn123@192.168.33.10:5672/wwxhost'


app = celery.Celery('tasks', broker=broker, backend=backend)
app.conf.update({
    'CELERY_TASK_SERIALIZER': 'json',
    'CELERY_RESULT_SERIALIZER': 'json',
    'CELERY_ACCEPT_CONTENT': 'json'
})


@app.task
def add(x, y):
    return x + y
