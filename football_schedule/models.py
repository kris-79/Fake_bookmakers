from django.db import models


# Create your models here.

class League(models.Model):
    name = models.CharField(max_length=20)
    logo = models.URLField(null=True)

    def __str__(self):
        return f'league: {self.name}'


class Team(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=40)
    form = models.CharField(max_length=5)
    logo = models.URLField(null=True)
    league = models.ForeignKey(League, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Player(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    country = models.CharField(max_length=40)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    goals = models.IntegerField(null=True)
    assists = models.IntegerField(null=True)
    injury = models.BooleanField()
    photo = models.URLField


class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name='home', on_delete=models.DO_NOTHING)
    away_team = models.ForeignKey(Team, related_name='away', on_delete=models.DO_NOTHING)
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=8)
    goals_home = models.IntegerField(null=True)
    goals_away = models.IntegerField(null=True)
    odds_home = models.FloatField(null=True, blank=True)
    odds_draw = models.FloatField(null=True, blank=True)
    odds_away = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.home_team} vs {self.away_team} ---> score:  {self.goals_home}:{self.goals_away}'
