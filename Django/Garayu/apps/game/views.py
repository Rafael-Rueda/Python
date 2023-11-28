from urllib.parse import urlencode

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from spotipy import Spotify, SpotifyException
from spotipy.oauth2 import SpotifyOAuth

from apps.rooms.models import Room, UserInRoom


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
        
def game_running(request, slug):
    if 'token_info' not in request.session:
        return HttpResponseBadRequest('Token information is missing.')
    
    token_info = request.session['token_info']
    
    sp = Spotify(auth=token_info['access_token'])

    playlists = sp.current_user_top_tracks() # Change this function based on the needs and modes of the game
        
    return JsonResponse({'playlists': playlists})
