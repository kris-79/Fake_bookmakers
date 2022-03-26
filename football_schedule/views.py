from django.shortcuts import render
from django.http import HttpResponse
from football_schedule.models import Team, Match, League, Player
from datetime import datetime
from django.views.generic import ListView, View





# Create your views here.

date_today = str(datetime.now())[0:10]
class MatchesAllView(View):
    def get(self, request):
        return render(
            request, template_name='matches_all.html',
            context={'matches': Match.objects.all()}
        )


class MatchesView(View):
    def get(self, request):
        return render(
            request, template_name='matches_today.html',
            context={'matches': Match.objects.filter(date__startswith=date_today).all()}
        )


# def welcome(request):
#     return render(request,
#                   template_name="base.html",
#                   context={'matches': Match.objects.filter(date__startswith='2022-03-20').all(),
#                            'leagues': League.objects.all()})


class MatchView(ListView):
    template_name = 'base.html'
    model = Match

# from football_schedule.models import Match
# query2 = Match.objects.filter(date__startswith='2022-03-13')
