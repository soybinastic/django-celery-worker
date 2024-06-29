from celery import shared_task


@shared_task(bind=True)
def process_track(self):
    # do some task here
    # ex. upload multiple big large objects to cloud storage

    for i in range(0, 5):
        print(str(i))

    return "DONE"


@shared_task(bind=True)
def process_periodic_task(self):
    # do some task here.
    return "Periodic task processed."