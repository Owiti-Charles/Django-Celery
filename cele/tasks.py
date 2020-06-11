from celery import shared_task
from time import sleep

from django.core.mail import send_mail

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_email():
    sleep(10)
    send_mail('Celery Trial',
    'The Trial must have worked.\n This is now done using celery',
    'pitchworld4@gmail.com',
    ['mikeycharlesm7@gmail.com','mikeycharles2@gmail.com']
    )
    return None

