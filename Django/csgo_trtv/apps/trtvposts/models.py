from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Comment(models.Model):
    text = models.TextField(max_length=3000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Polymorphism

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class CommentLike(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    comment = models.ForeignKey(to=Comment, on_delete=models.CASCADE)

class Post(models.Model):

    category_choices = [
        ('highlight', 'Highlight'),
        ('strategy', 'Strategy'),
        ('academy', 'Academy'),
        ('solo', 'Solo Play')
    ]

    map_choices = [
        ('de_ancient', 'Ancient'),
        ('de_anubis', 'Anubis'),
        ('de_cache', 'Cache'),
        ('de_dust2', 'Dust 2'),
        ('de_inferno', 'Inferno'),
        ('de_mirage', 'Mirage'),
        ('de_nuke', 'Nuke'),
        ('de_overpass', 'Overpass'),
        ('de_train', 'Train'),
        ('de_tuscan', 'Tuscan'),
        ('de_vertigo', 'Vertigo'),
        ('cs_agency', 'Agency (CS)'),
        ('cs_office', 'Office (CS)'),
    ]

    language_choices = [
        ('en', 'English'),
        ('pt', 'Portuguese'),
        ('ru', 'Russian'),
        ('sp', 'Spanish'),
    ]

    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='posts/covers/%Y/%m/%d')
    video = models.URLField(null=None, blank=None)
    description = models.TextField()
    category = models.CharField(max_length=12, choices=category_choices, default='highlight')
    map = models.CharField(max_length=16, choices=map_choices, default='de_ancient')
    language = models.CharField(max_length=24, choices=language_choices, default='en')
    slug = models.SlugField(unique=True, blank=None, null=None)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    comments = GenericRelation(Comment, related_name='comments')

    def __str__(self):
        return self.title
