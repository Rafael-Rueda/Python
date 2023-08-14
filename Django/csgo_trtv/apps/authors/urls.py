from django.urls import path

from apps.authors import views

app_name = 'authors'

urlpatterns = [
    path('login/',views.login, name='login'),  
    path('register/',views.register, name='register'),  
]
