from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
import logging

from django.contrib.auth.models import User

from . import models

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    users = User.objects.order_by('-id')[:5]
    context = {
        'users': users,
    }
    return render(request, 'menu.html', context)

def new(request):
    forum = models.Forum.objects.order_by('-creation')[:5]
    context = {
        'forum': forum,
    }
    return render(request, 'new.html', context)

def top(request):
    forum = models.Forum.objects.order_by('-upvotes')[:5]
    context = {
        'forum': forum,
    }
    return render(request, 'top.html', context)

def hot(request):
    forum = models.Forum.objects.annotate(num_comments=Count('comentary__forum')).order_by('-num_comments')[:5]
    context = {
        'forum': forum,
    }
    return render(request, 'hot.html', context)
