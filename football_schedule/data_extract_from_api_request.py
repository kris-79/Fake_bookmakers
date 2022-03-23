import json

# from datetime import datetime, timedelta
# str(datetime.now() + timedelta(hours=9))[11:19]
# '01:41:44'


with open('fixtures_today.json', 'r') as f:
    data = json.load(f)

data = data['response']
print(data)

match_date = (data[0]['fixture']['date'])[0:10]
country = data[0]['league']['country']
league = data[0]['league']['name']

matches_today = []
for line in data:
    home_team = line['teams']['home']['name']
    away_team = line['teams']['away']['name']
    match_time = (line['fixture']['date'])[11:19]
    score = (line['goals']['home'], line['goals']['away'])
    print(score)

    matches_today.append((home_team, away_team, match_time, score))

print()
print()
print()
print(f"Matches on {match_date}:")
print(20 * "------")
print(country, league)

for match in matches_today:
    if match[3][0] is None:
        print(f"{match[0]} vs {match[1]} {5 * ' '}at {match[2]}")

    else:
        print(f"{match[0]} vs {match[1]} {5 * ' '}  score  {match[3][0]}:{match[3][1]}")
