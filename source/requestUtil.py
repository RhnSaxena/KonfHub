import requests
import json


def requestGet(link):
    response = requests.get(link)
    return json.loads(response.text)
