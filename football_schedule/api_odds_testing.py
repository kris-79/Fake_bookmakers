import json
from pprint import pprint
from datetime import datetime
import requests

date_today = str(datetime.now())[0:10]
print(date_today)
leagues = {'french': 61, 'english': 39, 'german': 78, 'spanish': 140, 'italian': 135}

db_odds_by_date = []


def get_odds(date=date_today, league=39):
    url = "https://api-football-v1.p.rapidapi.com/v3/odds"

    querystring = {"date": date, "bet": 1, "bookmaker": 8, "season": 2021, "league": league}

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "2d85e84c38msh3751124afe15755p1823c5jsn3f010b502836"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response_json = response.json()
    response_json = response_json['response']
    # pprint(response_json, indent=3)

    db_data_odds = []

    for match in response_json:
        fixture_id = match['fixture']['id']
        odds = match['bookmakers'][0]['bets'][0]['values']
        odds_home = odds[0]['odd']
        odds_draw = odds[1]['odd']
        odds_away = odds[2]['odd']

        db_data_odds.append({'pk': fixture_id,
                             'model': 'football_schedule.odds',
                             'fields': {'home_win': odds_home,
                                        'draw': odds_draw,
                                        'away_team': odds_away,
                                        }})

    return db_data_odds

def get_all_odds():
    for league_name, league_id in leagues.items():
        all_odds_by_date = get_odds('2022-03-20', league_id)
        print(all_odds_by_date)
        return all_odds_by_date






if __name__ == '__main__':

    lista = get_all_odds()
    print(lista)

