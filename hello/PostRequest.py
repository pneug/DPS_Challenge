import requests
import django
from django.middleware.csrf import CsrfViewMiddleware, get_token
from django.test import Client

# Define the URL
url = "https://frozen-mesa-35935.herokuapp.com/"
body = {'name': 'John', 'age': '27'}

csrf_client = Client(enforce_csrf_checks=True)

# Retrieve the CSRF token first
csrf_client.get(URL)  # sets cookie
csrftoken = csrf_client.cookies['csrftoken']

# send a POST request
# r = requests.post(url, data=body, headers={'referer': url})
r = requests.post(url, data=body, headers=dict(Referer=url))
print("text" + str(r.text))
print("text" + str(r.status_code))
print("text" + str(r.headers))
print("text" + str(r.content))
