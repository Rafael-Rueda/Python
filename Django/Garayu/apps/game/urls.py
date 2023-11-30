from django.urls import path

from apps.game import views

app_name = 'game'

urlpatterns = [
    path('game/checking/<slug:slug>/', views.game_checking_available, name='game_checking'),
    path('game/start/<slug:slug>/', views.game_start, name='game_start'),
    path('game/running/<slug:slug>/', views.game_running, name='game_running'),
    path('game/sort/music/<slug:slug>', views.game_sort_music, name='game_sort_music'),
    path('game/ended/music/<slug:slug>', views.game_ended_music, name='game_ended_music'),
    path('game/end/music/<slug:slug>', views.game_end_music, name='game_end_music'),
]
