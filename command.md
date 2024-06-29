# command to run celery worker (--pool=solo is for debugging)
celery -A worker worker --pool=solo -l info
# or
celery -A worker worker -l info


# command to run celery beat
celery -A worker beat -l INFO