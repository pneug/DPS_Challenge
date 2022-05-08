from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import requests
import os


# Create your views here.
def index(request):
    # times = int(os.environ.get('TIMES', 3))
    return HttpResponse("Hello! " + request.body)
    # return HttpResponse('Hello! ' * 5)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def db_test(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
