from django.contrib import admin

from apps.game.models import PlaylistControl, QueueMusic

admin.site.register(PlaylistControl)
admin.site.register(QueueMusic)
