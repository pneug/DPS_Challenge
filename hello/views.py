from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

import requests
import os

# import the Challenge class from the python file Challenge.py
from .Challenge import Challenge


# Create your views here.
@csrf_exempt
def index(request):
    # times = int(os.environ.get('TIMES', 3))
    # convert the body in form of a json to a dictionary
    json_body = request.POST.dict()
    # return HttpResponse(str(json_body) + str(type(json_body)))
    # json_body = str(request.body)
    if not "month" in json_body:
        json_body["month"] = "1"
        #return HttpResponse("month is missing")
    if not "year" in json_body:
        json_body["year"] = "2021"
        # return HttpResponse("year is missing")

    challenge = Challenge()
    challenge.setup()
    date = datetime.strptime(json_body["year"] + "/" + json_body["month"], '%Y/%m')

    if "category" in json_body:
        prediction = challenge.get_prediction(date, json_body["category"])
    else:
        prediction = challenge.get_prediction(date)
    return HttpResponse("{\n\"prediction\":" + str(prediction[0]) + "\n}")
    # return HttpResponse('Hello! ' * 5)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

