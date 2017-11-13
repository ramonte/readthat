from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User

# Create your views here.
def index(request):
    users = User.objects.order_by('-id')[:5]
    context = {
        'users': users,
    }
    return render(request, 'menu.html', context)
