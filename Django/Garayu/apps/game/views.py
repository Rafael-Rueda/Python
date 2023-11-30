import time

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseGone, HttpResponseNotFound, JsonResponse)
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from spotipy import Spotify, SpotifyOAuth

from apps.game.models import PlaylistControl, QueueMusic
from apps.rooms.models import Room, UserInRoom


@csrf_exempt
@login_required(login_url='start:home')
def game_checking_available(request, slug):  
    room = Room.objects.filter(slug=slug).first()
    if not room.available:
        userinroom = UserInRoom.objects.filter(user=request.user).first()
        return JsonResponse({'started': True, 'is_host': userinroom.host})
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

@csrf_exempt
@login_required(login_url='start:home')
def game_running(request, slug):
    if 'token_info' not in request.session:
        return HttpResponseBadRequest('Token information is missing.')
    
    token_info = request.session['token_info']

    if token_info.get('expires_at', 0) < time.time():
            sp_oauth = SpotifyOAuth(
                settings.SPOTIFY_CLIENT_ID,
                settings.SPOTIFY_CLIENT_SECRET,
                settings.SPOTIFY_REDIRECT_URI,
                scope="user-library-read user-top-read user-read-playback-state user-read-recently-played",
            )
            token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
            request.session['token_info'] = token_info
    
    sp = Spotify(auth=token_info['access_token'])

    room = Room.objects.filter(slug=slug).first()

    playlists = sp.current_user_saved_tracks(limit=50) # Change this function based on the needs and modes of the game

    players_data = [{'user': player.user.username,'nickname': player.user.first_name, 'host': player.host} for player in UserInRoom.objects.filter(room=room)]

    current_username = request.user.username

    if not PlaylistControl.objects.filter(user=request.user, room=room).exists():
        for track in playlists['items']:
            PC_instance = PlaylistControl.objects.create(user=request.user,
                                        room=room,
                                        playlist_preview_url=track['track']['preview_url'], 
                                        playlist_cover=track['track']['album']['images'][1]['url'], 
                                        playlist_name=track['track']['name'],
                                        playlist_artist=track['track']['artists'][0]['name']
                                        )
            PC_instance.save()

    queue = QueueMusic.objects.filter(room=room).first()

    # return JsonResponse({'playlists': playlists, 'players': players_data, 'current_username': current_username})
    if queue and queue.queue:
        music_src = queue.queue.playlist_preview_url
        music_cover = queue.queue.playlist_cover
        music_name = queue.queue.playlist_name
        artist = queue.queue.playlist_artist

        return JsonResponse({'music_src': music_src, 'music_cover': music_cover, 'music_name': music_name, 'music_artist': artist})
    else:
        return HttpResponseNotFound()

@csrf_exempt
@login_required(login_url='start:home')
def game_sort_music(request, slug):
    if request.method == 'POST':
        room = Room.objects.filter(slug=slug).first()

        has_track = PlaylistControl.objects.filter(blacklisted=False).first()

        # Cant use session because it is individual
        # request.session['queue_music'] = {'track': random_track.playlist_preview_url, 'cover': random_track.playlist_cover, 'name': random_track.playlist_name}
        if has_track:
            if not QueueMusic.objects.filter(room=room).exists():
                track = PlaylistControl.objects.filter(room=room, blacklisted=False).order_by('?').first()
                
                queue_music = QueueMusic.objects.create(room=room, queue=track)
                queue_music.save()

                track.blacklisted = True
                track.save()
            else:
                track = PlaylistControl.objects.filter(room=room, blacklisted=False).order_by('?').first()

                queue_music = QueueMusic.objects.filter(room=room).first()
                queue_music.queue = track
                queue_music.ended = False
                queue_music.save()

                track.blacklisted = True
                track.save()

        return redirect('game:game_running', slug=slug)
    else:
        return redirect('rooms:rooms_joining', slug=slug)

@csrf_exempt
@login_required(login_url='start:home')
def game_ended_music(request, slug):
    if request.method == 'POST':
        room = Room.objects.filter(slug=slug).first()
        queue_music = QueueMusic.objects.filter(room=room).first()
        if room:
            if queue_music:
                if queue_music.ended:
                    return redirect('game:game_checking', slug=slug)
                else:
                    return JsonResponse({'started': False})
            else:
                return JsonResponse({'started': False})
        else:
            return redirect('rooms:rooms')

    else:
        return redirect('rooms:rooms_joining', slug=slug)

@csrf_exempt
@login_required(login_url='start:home')
def game_end_music(request, slug):
    if request.method == 'POST':
        room = Room.objects.filter(slug=slug).first()
        queue_music = QueueMusic.objects.filter(room=room).first()
        queue_music.ended = True
        queue_music.save()
        return redirect('game:game_checking', slug=slug)
    else:
        return redirect('rooms:rooms_joining', slug=slug)