from django.urls import path

from apps.plays import views

app_name = 'plays'

urlpatterns = [
    path('', views.home , name='home'),
    path('highlights', views.highlights, name='highlights'),
    path('strategies', views.strategies, name='strategies'),
    path('academy', views.academy, name='academy'),
    path('category/<str:category>', views.bycategory, name='bycategory'),
    path('map/<str:map>', views.bymap, name='bymap'),
]
