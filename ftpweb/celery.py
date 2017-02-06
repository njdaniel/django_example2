""""Celery module for Automating
Setting Up to use celery:
    Using settings.py for the celery app settings,
        using 'CELERY_'

    Create instance of Celery, and discover tasks that automatically discovered in the
        tasks.py (It's MAGIC!!)
"""

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ftpweb.settings')

app = Celery('ftpweb')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))