from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

import requests

def index(request):
    response = requests.get(settings.API_URL)
    posts = response.json()
    total_responses = len(posts)
    # total_responses = 0
    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses
    }
    return render(request, "dashboard/index.html", data)
