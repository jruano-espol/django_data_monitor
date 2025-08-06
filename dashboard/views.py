from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import requests

@login_required
def index(request):
    response = requests.get(settings.API_URL)
    posts = response.json()
    total_responses = len(posts)

    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses
    }
    return render(request, "dashboard/index.html", data)
