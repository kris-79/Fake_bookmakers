import json
from pprint import pprint

todays_fixtures = []

"""Getting response_data and extracting fixtures(values) of relevant leagues"""


def get_todays_matches():
    with open('response_matches.json') as file:
        response_data = json.load(file)

    for k, v in response_data.items():
        if k == 'response':
            for match in v:
                for key, value in match.items():
                    # filtering fixtures by league id
                    if key == 'league' and value['id'] == 39 \
                            or key == 'league' and value['id'] == 61 \
                            or key == 'league' and value['id'] == 78 \
                            or key == 'league' and value['id'] == 135 \
                            or key == 'league' and value['id'] == 41 \
                            or key == 'league' and value['id'] == 140:
                        todays_fixtures.append(match)

    #  sorting today's matches by league and kick-off time
    fixtures = sorted(todays_fixtures, key=lambda x: (x['league']['id'], x['fixture']['date']))
    return fixtures


if __name__ == '__main__':

    sorted_fixtures = get_todays_matches()
    for fixture in sorted_fixtures:
        print(f"{fixture['teams']['home']['name']} vs {fixture['teams']['away']['name']}"
              f" at {fixture['fixture']['venue']['name']}"
              f"  {fixture['fixture']['date'][11:16]}\nresult   "
              f"{fixture['goals']['home']}:{fixture['goals']['away']}")
