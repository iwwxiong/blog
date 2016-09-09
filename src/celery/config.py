# Celery 配置（以下是一些常用设置，celery默认配置基本就能满足我们大部分需求）

# 可接受内容格式
CELERY_ACCEPT_CONTENT = 'json'

# worker执行任务后死掉， 默认无限制
# CELERYD_MAX_TASKS_PER_CHILD = 10

## Task settings 任务配置

# 设置example1_tasks中add方法每秒最多执行10次。
CELERY_ANNOTATIONS = {
    'example1_tasks.add': {
        'rate_limit': '10/s'
    }
}

# task序列化
CELERY_TASK_SERIALIZER = 'json'

## Concurrency settings 并发性配置

# worker并发数 默认等于CPUS
# CELERYD_CONCURRENCY = 50

# 每次去broker中获取任务数，默认为4个（官方推荐。）
# CELERYD_PREFETCH_MULTIPLIER = 4

## Task result backend settings task结果backend配置

# result backend
# 可选择：database，cache，mongodb，redis，amqp，cassandra，irocache，couchbase
CELERY_RESULT_BACKEND = 'amqp'  # 官方推荐amqp 

# 结果序列
CELERY_RESULT_SERIALIZER = 'json'

# 结果backend选择SQLAlchemy database的时候可选配置
# CELERY_RESULT_ENGINE_OPTIONS = {'echo': True}

## AMQP backend settings amqp协议backend配置

# 结果exchange， 默认 celeryresult
# CELERY_RESULT_EXCHANGE = ''

# 结果默认exchange_type为direct
# CELERY_RESULT_EXCHANGE_TYPE = ''

# 结果持久化，设置为True， 消息结果不会因为broker重启后丢失。
CELERY_RESULT_PERSISTENT = True

# 任务超时时间
CELERY_TASK_RESULT_EXPIRES = 1000*18  # s

## Message Routing 消息路由
# 默认的queue/exchange/binding_key为celery，默认exchange_type为direct

# celery队列
# CELERY_QUEUES = ''

# celery路由
# CELERY_ROUTES = ''

# queue高可用（RabbitMQ）,默认为'all'
# 如果设置为'all'， 则会复制队列到所有的节点
# CELERY_QUEUE_HA_POLICY = ['rabbit@host1', 'rabbit@host2']

# .apply_async默认使用queue
# CELERY_DEFAULT_QUEUE = ''

# 未自定义CELERY_QUEUES时，下面默认使用
# 默认exchange
CELERY_DEFAULT_EXCHANGE = 'celery'

# 默认exchange_type
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'

# 默认routing_key
CELERY_DEFAULT_ROUTING_KEY = 'celery'

## Broker Settings Broker设置

# Broken地址
BROKER_URL = 'amqp://username:password@host:port/vitual_host'

# broker连接超时（默认4s）
BROKER_CONNECTION_TIMEOUT = 4

## Worker

# tasks任务导入
CELERY_IMPORTS = ('example1_tasks','example2_tasks',)