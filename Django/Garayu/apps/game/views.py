from django.shortcuts import render, redirect
from apps.rooms.models import Room, UserInRoom
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

@csrf_exempt
@login_required(login_url='start:home')
def game_checking_available(request, slug):
    if not request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return HttpResponseBadRequest('Invalid request')
    
    room = Room.objects.filter(slug=slug).first()
    if not room.available:
        return JsonResponse({'started': True})
    else:
        return JsonResponse({'started': False})


@csrf_exempt
@login_required(login_url='start:home')
def game_start(request, slug):
    if not request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return HttpResponseBadRequest('Invalid request')
    if request.method == 'POST':
        room = Room.objects.filter(slug=slug).first()
        room.available = False
        room.save()
        return JsonResponse({})
    else:
        messages.error(request, 'An error occurred while starting the game.')
        return redirect('rooms:rooms_joining', slug=slug)
        