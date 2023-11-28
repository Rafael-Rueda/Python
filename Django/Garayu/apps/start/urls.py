from django.urls import path
from apps.start import views

app_name = 'start'

urlpatterns = [
    path('', views.home, name='home')
]
