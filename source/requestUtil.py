import requests
import json

# Function that a link as a string parameter,
# performs GET operation on the link
# and returns the response.
def requestGet(link):
    response = requests.get(link)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print("Some error occured. Please check the link")
        exit()
