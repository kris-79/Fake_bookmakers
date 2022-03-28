from django.urls import path
from .views import MatchView, MatchesView, MatchesAllView, CreateBetView


urlpatterns = [
    path('', MatchesAllView.as_view(), name='matches_all'),
    path('today/', MatchesView.as_view(), name='matches_today'),
    path('bet/', CreateBetView.as_view(), name='place_a_bet'),
]
