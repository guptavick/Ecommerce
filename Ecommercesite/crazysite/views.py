from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


def index(request):
    products = Product.objects.all()
    product_count = Product.objects.all().count()
    slide_count = (product_count//4) + ceil((product_count/4)-product_count//4)
    return render(request, 'crazysite/index.html', {'products':products,'slide_count':slide_count, 'range': range(1,slide_count)})

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