from __future__ import absolute_import,unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','Test.settings')

app = Celery('Test')
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()

# celer beat    
app.conf.beat_schedule={

}



@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')



