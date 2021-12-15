from django.shortcuts import render
from redis import Redis
from redis.sentinel import Sentinel
from django.core.cache import cache

def home(request):
    if cache.get('visit'):
        data = "Visiting after 15 minutes"
    else:
        data = data = "Visiting before 15 minutes"
        cache.set('visit', 'visited', timeout = 15* 60)
    return render(request, 'home.html')
