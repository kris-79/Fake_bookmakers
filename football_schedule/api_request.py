import requests
import json
from pprint import pprint
from datetime import datetime


current_date = str(datetime.now())[0:10]
# print(current_date)
# current_date = '2022-03-13'

# league names by id
leagues = {'french': 61, 'english': 39, 'german': 78, 'spanish': 140, 'italian': 135}

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

querystring = {"date": current_date, "league": leagues['spanish'], "season": "2021"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "2d85e84c38msh3751124afe15755p1823c5jsn3f010b502836"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
response_json = response.json()


with open("fixtures_today.json", "w") as todays_fixture:
    json.dump(response_json, todays_fixture, indent=3)

if __name__ == '__main__':
    pprint(response_json)
    print(type(response_json))
