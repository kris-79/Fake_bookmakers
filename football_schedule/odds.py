import json

import requests
from pprint import pprint

url = "https://api-football-v1.p.rapidapi.com/v3/odds"

querystring = {"date":"2022-03-19"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "2d85e84c38msh3751124afe15755p1823c5jsn3f010b502836"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
odds_response = response.json()

with open('odds_by_date.json', 'w') as file:
    json.dump(odds_response, file, indent=3)
# pprint(odds_response, indent=3)