from api_request_odds import get_odds_by_date
from data_from_api_matches import get_todays_matches
from pprint import pprint
import json


sorted_matches = get_todays_matches()
db_odds = get_odds_by_date()
print(f'db_odds  {db_odds}')
db_data = []

for match in sorted_matches:
    # pprint(match, indent=3)

    db_data.append({'pk': match['fixture']['id'],
                    'model': 'football_schedule.match',
                    'fields': {'home_team': match['teams']['home']['id'],
                               'away_team': match['teams']['away']['id'],
                               'date': match['fixture']['date'][0:10],
                               'time': match['fixture']['date'][11:16],
                               'goals_home': match['goals']['home'],
                               'goals_away': match['goals']['away'],
                               # 'league-position':
                               }})

    db_data.append({'pk': match['teams']['home']['id'],
                    'model': 'football_schedule.team',
                    'fields': {'name': match['teams']['home']['name'],
                               'country': match['league']['country'],
                               'form': 'WWWWW',
                               'logo': match['teams']['home']['logo'],
                               'league': match['league']['id'],

                               }})

    db_data.append({'pk': match['teams']['away']['id'],
                    'model': 'football_schedule.team',
                    'fields': {'name': match['teams']['away']['name'],
                               'country': match['league']['country'],
                               'form': 'WWWWW',
                               'logo': match['teams']['away']['logo'],
                               'league': match['league']['id'],

                               }})
    db_data.append({'pk': match['league']['id'],
                    'model': 'football_schedule.league',
                    'fields': {'name': match['league']['name'],
                               'logo': match['league']['logo'],
                               }})
# print(f'db_data  {db_data}')

for match in db_data:
    if match['model'] == 'football_schedule.match':
        print(f"match_pk {match['pk']}")
        for odds in db_odds:
            if match['pk'] == odds['pk']:
                match['fields']['odds_home'] = odds['home_win']
                match['fields']['odds_draw'] = odds['draw']
                match['fields']['odds_away'] = odds['away_win']
                print(f"{match['fields']['home_team']} odds to win are {odds['home_win']}")
                print("succes!!!!!!!!!!")




pprint(db_data, indent=2)


with open('db_load.json', 'w') as file:
    json.dump(db_data, file, indent=3)
