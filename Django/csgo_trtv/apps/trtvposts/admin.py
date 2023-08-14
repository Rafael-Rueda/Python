from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from apps.trtvposts import models


class CommentInline(GenericStackedInline):
    model = models.Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'video')
    list_editable = ('slug', 'video')
    inlines = [
        CommentInline
    ]

admin.site.register(models.Post, PostAdmin)

admin.site.register(models.Comment)