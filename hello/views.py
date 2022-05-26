from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

import requests
import os
import json

# import the Challenge class from the python file Challenge.py
from .Challenge import Challenge


curr_room = 0
stat_dict = {}


# Create your views here.
@csrf_exempt
def index(request):
    global curr_room
    global stat_dict

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

    if "room_nr" in json_body:
        curr_room = json_body["room_nr"]
        stat_dict["room_nr"] = json_body["room_nr"]

    if "playerCount" in json_body:
        stat_dict["playerCount"] = json_body["playerCount"]
        try:
            for i in range(stat_dict["playerCount"]):
                stat_dict["player_" + str(i)] = json_body["player_" + str(i)]
        except e:
            stat_dict["error"] = str(e)

    challenge = Challenge()
    challenge.setup()
    date = datetime.strptime(json_body["year"] + "/" + json_body["month"], '%Y/%m')

    if "category" in json_body:
        prediction = challenge.get_prediction(date, json_body["category"])
    else:
        prediction = challenge.get_prediction(date)

    response = stat_dict.copy()
    response["prediction"] = prediction[0]
    response = json.dumps(response)
    return HttpResponse(response)
    # return HttpResponse("{\n\"prediction\":" + str(prediction[0]) +
    #                     "\"room_nr\": " + str(curr_room) +
    #                     "\n}")
    # return HttpResponse('Hello! ' * 5)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def stats(request):
    return HttpResponse("{\n\"prediction\":" + str(prediction[0]) + "\n}")

