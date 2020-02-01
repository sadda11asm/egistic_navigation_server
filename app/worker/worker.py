import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('tasks', backend='rpc://', broker='pyamqp://')
app.conf.update(settings.CELERY)
