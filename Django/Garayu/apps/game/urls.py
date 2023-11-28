from django.urls import path
from apps.game import views

app_name = 'game'

urlpatterns = [
    path('game/checking/<slug:slug>', views.game_checking_available, name='game_checking'),
    path('game/start/<slug:slug>', views.game_start, name='game_start'),
]
