from django.urls import path

from .views import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_api, name='posts'),
]