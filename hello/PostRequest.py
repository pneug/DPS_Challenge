import requests
import django
from django.middleware.csrf import CsrfViewMiddleware, get_token
from django.test import Client

# Define the URL
url = "https://frozen-mesa-35935.herokuapp.com/"
body = {
    "year":2020,
    "month":10
}

# send a POST request
r = requests.post(url, data=body, headers=dict(Referer=url))
print(str(r.text))
print("Code: " + str(r.status_code))
