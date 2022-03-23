from pprint import pprint
import json

# from datetime import datetime, timedelta
# str(datetime.now() + timedelta(hours=9))[11:19]
# '01:41:44'


with open('fixtures_today.json', 'r') as f:
    schedule = json.load(f)

schedule = schedule['response']

match_date = (schedule[0]['fixture']['date'])[0:10]

country = schedule[0]['league']['country']
league = schedule[0]['league']['name']
league_id = schedule[0]['league']['id']

matches_today = [{'pk': schedule[0]['league']['id'], 'model': 'football_schedule.league',
                  'fields': {'name': league,
                             'logo': schedule[0]['league']['logo']}}]

for line in schedule:
    home_team_id = line['teams']['home']['id']
    home_team_name = line['teams']['home']['name']
    away_team_id = line['teams']['away']['id']
    away_team_name = line['teams']['away']['name']
    match_time = (line['fixture']['date'])[11:19]
    score = (line['goals']['home'], line['goals']['away'])
    pk_match = line['fixture']['id']
    home_team_logo = line['teams']['home']['logo']
    away_team_logo = line['teams']['away']['logo']


    matches_today.append({'pk': pk_match, 'model': 'football_schedule.match', 'fields': {'home_team': home_team_id,
                                                                                         'away_team': away_team_id,
                                                                                         'date': match_date,
                                                                                         'time': match_time,
                                                                                         'goals_home': score[0],
                                                                                         'goals_away': score[1]
                                                                                         }})

    matches_today.append({'pk': home_team_id, 'model': 'football_schedule.team', 'fields': {'name': home_team_name,
                                                                                            'country': country,
                                                                                            'form': 'WWWWW',
                                                                                            'logo': home_team_logo,
                                                                                            'league': league_id,

                                                                                            }})

    matches_today.append({'pk': away_team_id, 'model': 'football_schedule.team', 'fields': {'name': away_team_name,
                                                                                            'country': country,
                                                                                            'form': 'WWWWW',
                                                                                            'logo': away_team_logo,
                                                                                            'league': league_id,

                                                                                            }})

pprint(matches_today, indent=3)
with open('load_matches.json', 'w') as file:
    json.dump(matches_today, file, indent=3)
