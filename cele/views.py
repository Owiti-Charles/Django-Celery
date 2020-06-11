from django.shortcuts import render
from django.http import HttpResponse
from .tasks import sleepy, send_email

def index(request):
    send_email.delay()
    return HttpResponse('<h1>Sent Succesfully using Celery</h1>')
