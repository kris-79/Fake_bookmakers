from django.urls import path
from .views import MatchView, MatchesView, MatchesAllView


urlpatterns = [
    path('', MatchView.as_view(), name='matches'),
    path('all/', MatchesAllView.as_view(), name='matches_test'),
    path('today/', MatchesView.as_view(), name='matches_test')
]
