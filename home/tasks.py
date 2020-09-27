from celery import shared_task


@shared_task
def add_test(a, b):
    return a + b
