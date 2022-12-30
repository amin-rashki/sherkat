from argparse import Namespace
from celery import Celery
from celery.schedules import crontab

app = Celery()

app.conf.beat_schedule = {
    # Execute daily at midnight
    'add-every-daily-midnight': {
        'task': 'tasks.add',
        'schedule': crontab(minute=0, hour=0)
    },
}

app.config_from_object('django.conf:settings',namespace='CELERY')