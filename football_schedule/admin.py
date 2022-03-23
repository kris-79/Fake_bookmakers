from django.contrib import admin
from .models import Team, Match, League
# Register your models here.
admin.site.register(League)
admin.site.register(Match)
admin.site.register(Team)