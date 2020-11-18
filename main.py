from requests_function import request_get
from readable import refine
from config import link
import json
from replicas import createMap


def driver():
    response = request_get(link)
    print(refine(response))
    h= createMap(response)
    jsonText = json.dumps(h)
    f = open("dict.json","w")
    f.write(jsonText)
    f.close()

driver()