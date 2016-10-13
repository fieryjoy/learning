import os
from celery import Celery

BROKER_URL=os.environ['BROKER_URL']
BACKEND_URL=os.environ['BACKEND_URL']

app = Celery('hello',
#             backend='rpc://',
             backend=BACKEND_URL, 
             broker=BROKER_URL)

app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT = ['application/json'],
    CELERY_RESULT_SERIALIZER = 'json'
)

