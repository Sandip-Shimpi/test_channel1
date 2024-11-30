from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_channel.settings')

# Create an instance of Celery
app = Celery('test_channel')

# Load configuration from Django settings, using a 'CELERY_' namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks from all registered Django app configs.
app.autodiscover_tasks()
#
#@app.task(bind=True)
#def debug_task(self):
#    print(f'Request: {self.request!r}')
