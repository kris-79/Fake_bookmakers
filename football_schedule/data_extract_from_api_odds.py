import json
from pprint import pprint

with open('odds_by_date.json', 'r') as file:
    odds_response = json.load(file)

# pprint(odds_response)


def get_todays_matches():
    todays_odds = []
    for k, v in odds_response.items():
        if k == 'response':
            print(k)
            for match in v:
                # print(f'match{match}')

                for key, value in match.items():
                    # filtering fixtures by league id
                    print(key)
                    if key == 'league' : #\
                        print(value['id'])
                    #         or key == 'league' and value['id'] == 61 \
                    #         or key == 'league' and value['id'] == 78 \
                    #         or key == 'league' and value['id'] == 135 \
                    #         or key == 'league' and value['id'] == 140:
                    #     todays_odds.append(match)

    #  sorting today's matches by league and kick-off time
    # fixtures = sorted(todays_odds, key=lambda x: (x['league']['id'], x['fixture']['date']))
    # return fixtures

if __name__ == '__main__':
    odds = get_todays_matches()
    print(odds)
