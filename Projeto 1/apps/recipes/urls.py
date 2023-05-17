from django.urls import path
from apps.recipes import views

urlpatterns = [
    path('', views.Home)    
]
