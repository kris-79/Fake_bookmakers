from django.urls import path
from .views import MatchView, MatchesView


urlpatterns = [
    path('', MatchView.as_view(), name='matches'),
    path('testing/', MatchesView.as_view(), name='matches_test')
]
