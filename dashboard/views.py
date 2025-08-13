from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import requests
import time


def get_product_counts(data):
    product_counts = {}
    for entry in data.values():
        product_id = entry.get('productID', '')
        if product_id:
            if product_id in product_counts:
                product_counts[product_id] += 1
            else:
                product_counts[product_id] = 1
    return product_counts


def get_most_common_product(product_counts):
    if not product_counts:
        return None, 0
    most_common_product, highest_count = None, 0
    for product, count in product_counts.items():
        if count > highest_count:
            highest_count = count
            most_common_product = product

    return most_common_product, highest_count


#@login_required
def index(request):
    start_time = time.time()
    response = requests.get(settings.API_URL)
    posts = response.json()
    end_time = time.time()

    duration_ms = (end_time - start_time) * 1000  # Convert to milliseconds
    total_responses = len(posts)
    product_counts = get_product_counts(posts)
    most_common_product, most_common_product_count = get_most_common_product(product_counts)

    data = {
        'title': "Landing Page Dashboard",
        'posts': posts,
        'total_responses': total_responses,
        'duration_ms': f'{duration_ms:.4f}',
        'most_common_product': most_common_product,
        'most_common_product_count': most_common_product_count,
    }
    return render(request, "dashboard/index.html", data)
