import json
from pprint import pprint
from datetime import datetime
import requests
from api_request_odds import date_today

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

querystring = {"date": date_today}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "2d85e84c38msh3751124afe15755p1823c5jsn3f010b502836"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
response_to_json = response.json()
print(response_to_json)

with open('response_to_json_v2.json', 'w') as file:
    json.dump(response_to_json, file, indent=3)

print(response_to_json)


