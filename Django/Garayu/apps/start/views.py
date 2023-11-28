from django.shortcuts import render
from apps.rooms import models
from apps.start import forms

def home(request):
    rooms_available = models.Room.objects.all().count()
    
    if 'nicknamedata' in request.session:
        form = forms.NicknameForm(request.session['nicknamedata'])
        del request.session['nicknamedata']
    else:
        form = forms.NicknameForm()

    return render(request, 'start/pages/homepage.html',{'rooms_available': rooms_available, 'form': form})
