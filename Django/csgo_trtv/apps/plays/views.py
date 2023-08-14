from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import render

from apps.trtvposts.models import Post


def home(request):
    posts = Post.objects.order_by('-id').filter(is_published = True)[:10]
    return render(request, 'plays/pages/home.html', {'posts': posts})

def highlights(request):
    posts = Post.objects.filter(Q(category = 'highlight') | Q(category = 'solo')).order_by('-id').filter(is_published = True)
    return render(request, 'plays/pages/highlights.html', {'posts': posts})
def strategies(request):
    posts = Post.objects.filter(category = 'strategy').order_by('-id').filter(is_published = True)
    return render(request, 'plays/pages/strategies.html', {'posts': posts})
def academy(request):
    posts = Post.objects.filter(category = 'academy').order_by('-id').filter(is_published = True)
    return render(request, 'plays/pages/academy.html', {'posts': posts})

def bycategory(request, category):
    posts = Post.objects.filter(category=category).order_by('-id').filter(is_published = True)
    if not posts:
        raise Http404
    return render(request, 'plays/pages/filterposts.html', {'posts': posts, 'title': category})
def bymap(request, map):
    posts = Post.objects.filter(map=map).order_by('-id').filter(is_published = True)
    if not posts:
        raise Http404
    return render(request, 'plays/pages/filterposts.html', {'posts': posts, 'title': map})