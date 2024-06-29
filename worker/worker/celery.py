from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from django.conf import settings

"""Import crontab schedule for celery beat"""
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'worker.settings')

app = Celery(__name__)

# not necessary for now, just comment it 
# app.conf.enable_utc = False

app.config_from_object(settings, namespace='CELERY')

app.conf.timezone = 'Asia/Chongqing'

# Celery beat settings (Periodic task)
app.conf.beat_schedule = {
    # it will execute every 9:26 PM with Asia/Chongqing timezone
    'my_periodic_task' : {
        'task' : 'tracks.tasks.process_periodic_task',
        'schedule' : crontab(hour=21, minute=36),
        # 'args' : 
    }
}


app.autodiscover_tasks()

@app.task(bind=True)
def my_task(self):
    print(f'TASK: {self.request!r}')
