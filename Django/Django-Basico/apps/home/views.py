from django.shortcuts import render
from apps.schedule import models

def home(request):
    if request.user.is_authenticated:
        schedules = models.schedule.objects.get_user_schedules(request.user)
    else:
        schedules = []

    return render(request, 'home/pages/home.html', {'schedules': schedules})