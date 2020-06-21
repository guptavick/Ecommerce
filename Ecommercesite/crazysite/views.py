from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


def index(request):
    categories = Product.objects.values_list('category', flat = True).distinct()
    allprods = []
    for cat in categories:
        products = Product.objects.filter(category = cat)
        product_count = len(products)
        slide_count = (product_count//4) + ceil((product_count/4)-product_count//4)

        allprods.append([products, range(1, slide_count), slide_count])

    return render(request,  'crazysite/index.html', {'allprods':allprods})

def aboutus(request):
    return render(request, 'crazysite/about.html')

def contactus(request):
    return HttpResponse('you viewing contact us page')

def search(request):
    return HttpResponse('you viewing search page')

def product(request):
    return HttpResponse('you viewing product detail page')

def ordertracking(request):
    return HttpResponse('you are viewing order tracking page')

def checkout(request):
    return HttpResponse('you are viewing checkout page')