from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count
from django.utils import timezone
from django.contrib.auth.views import login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy, reverse

import logging

from django.contrib.auth.models import User

from . import forms
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
    forum = models.Forum.objects.annotate(num_comments=Count('comment__forum')).order_by('-creation')
    context = {
        'forum': forum,
    }
    return render(request, 'lista.html', context)

def top(request):
    forum = models.Forum.objects.order_by('-upvotes')
    context = {
        'forum': forum,
    }
    return render(request, 'lista.html', context)

def hot(request):
    forum = models.Forum.objects.annotate(num_comments=Count('comment__forum')).order_by('-num_comments')
    context = {
        'forum': forum,
    }
    return render(request, 'lista.html', context)

def details(request, forum_id):
    forum = get_object_or_404(models.Forum, pk=forum_id)
    if request.POST:
        form = forms.CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user = request.user
            comment.date = timezone.now()
            comment.forum = forum
            comment.save()
    form = None
    form = forms.CommentForm()
    form.description = ''
    comments = models.Comment.objects.filter(forum=forum_id)
    context = {
        'forum': forum,
        'comments': comments,
        'form': form,
    }
    return render(request, 'details.html', context)

def new_post(request):
    if request.method == 'POST':
        form = forms.ForumForm(request.POST)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.user = request.user
            forum.creation = timezone.now()
            forum.save()
            ff = get_object_or_404(models.Forum, pk=forum.pk)
            comments = models.Comment.objects.filter(forum=forum.pk)
            context = {
                'forum': ff,
                'comments': comments,
            }
            return render(request, 'details.html', context)
    else:
        form = forms.ForumForm()
    return render(request, 'new_post.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'menu.html', {})
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('new'))

    kwargs['extra_context'] = {'next': reverse('new')}
    kwargs['template_name'] = 'login.html'
    return login(request, *args, **kwargs)


def logout_view(request, *args, **kwargs):
    kwargs['next_page'] = reverse('new')
    return logout(request, *args, **kwargs)

def results(request):
    search = request.GET.get('search')
    forum = models.Forum.objects.annotate(num_comments=Count('comment__forum')).filter(title__icontains=search)
    forum = forum | models.Forum.objects.annotate(num_comments=Count('comment__forum')).filter(description__icontains=search)
    context = {
        'forum': forum,
    }
    return render(request, 'results.html', context)
