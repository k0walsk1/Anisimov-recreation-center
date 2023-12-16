from django.urls import path
from . import  views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('journeys', views.journeys, name='journeys'),
    path('games', views.games, name='games'),
    path('entertainments', views.entertainments, name='entertainments'),
]