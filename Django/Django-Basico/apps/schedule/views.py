from django.shortcuts import render, redirect
from apps.schedule.forms import ScheduleForm
from apps.schedule.models import schedule
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def create_schedule(request):
    if request.method == 'GET':
        if 'data-schedule' in request.session:
            form = ScheduleForm(request.session['data-schedule'])
            del(request.session['data-schedule'])
        else:
            form = ScheduleForm()
        return render(request, 'schedule/pages/create-schedule.html', {'form': form})
    elif request.method == 'POST':
        request.session['data-schedule'] = request.POST
        modelform = ScheduleForm(request.POST)

        if modelform.is_valid():
            save = modelform.save(commit=False)
            save.author = request.user
            save.save()
            return redirect('home:home')
    return redirect('schedule:create_schedule')

def search(request):
    search_term = request.GET['q'].strip()
    schedules = schedule.objects.filter(Q(phone__icontains = search_term) | Q(first_name__icontains = search_term) | Q(last_name__icontains = search_term) | Q(email__icontains = search_term))
    return render(request, 'home/pages/home.html', {'schedules': schedules})

@login_required
def edit_schedule(request, schedule_id):
    instance = schedule.objects.get(id = schedule_id) 
    if request.method == 'POST':
        modelform = ScheduleForm(request.POST, instance=instance)
        if modelform.is_valid():
            modelform.save()
        return redirect('schedule:edit_schedule', schedule_id) 
    form = ScheduleForm(instance = instance)
    return render(request, 'schedule/pages/edit-schedule.html', {'form': form, 'schedule_id': schedule_id})