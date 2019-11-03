from __future__ import absolute_import, unicode_literals
from celery import Celery
import os


# https://medium.com/@yedjoe/celery-4-periodic-task-in-django-9f6b5a8c21c7



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

app = Celery('django_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


