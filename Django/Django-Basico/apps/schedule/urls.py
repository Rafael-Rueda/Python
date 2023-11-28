from django.urls import path
from apps.schedule import views

app_name = 'schedule'

urlpatterns = [
    path('create-schedule/', views.create_schedule, name='create_schedule'),
    path('search/', views.search, name='search'),
    path('edit-schedule/<int:schedule_id>', views.edit_schedule, name='edit_schedule')
]
