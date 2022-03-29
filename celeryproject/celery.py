from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# setting the Django settings module.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryproject.settings')

app = Celery('celeryproject',include=['celeryproject.celery'],broker=settings.CELERY_BROKER_URL,backend=settings.CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY') 

app.conf.beat_schedule = {
    'send_mail' : {
        'task':'celeryapp.task.send_email',
        'schedule':5,
    }
}

# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks()