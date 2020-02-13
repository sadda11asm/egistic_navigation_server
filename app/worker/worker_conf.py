import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('tasks', backend='rpc://', broker="amqp://patriot:GtzYz4ahBvR3THg6x89E7wpNDCtYGLCZt6LSqZNXWaerEqD3bdkxRqTjZ6DFjL6Z@rabbitmq:5672")
app.conf.update(settings.CELERY)
app.conf.update(
	ENABLE_UTC=True,
	TIMEZONE='Asia/Almaty')

#app.conf.CELERY_TIMEZONE = 'Asia/Almaty'
