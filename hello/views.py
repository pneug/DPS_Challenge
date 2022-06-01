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

room_settings = {}

default_room_0 = {
    "roomName": "Lobby",
    "roomTitle": "Lobby",
    "roomVersion": 0
}

default_room_1 = {
    "roomName": "NetworkingArea",
    "roomTitle": "Networking Area",
    "roomVersion": 1
}
default_rooms = [default_room_0, default_room_1]


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
        for i in range(int(stat_dict["playerCount"])):
            stat_dict["player_" + str(i)] = json_body["player_" + str(i)]

    if "setRoomSettings" in json_body:
        pass

    if "GetSpawnRoom" in json_body:
        response = default_rooms[len(Greeting.objects.all()) % 2]
        # response = {"roomName": 1 + len(Greeting.objects.all()) % 2}
        # response["Num greetings"] = len(Greeting.objects.all())
    else:
        response = stat_dict.copy()

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

