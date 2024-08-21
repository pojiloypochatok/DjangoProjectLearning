from django.shortcuts import render
from django.core.paginator import Paginator

from goods.models import Categories, Products
from goods.utils import q_search

# Create your views here.

def courses(request):

    context = {
        'title': 'Choose Your Side!',
    }
    return render(request, 'goods/courses.html', context)
    #paginator = Paginator(goods, 2)


def backend(request):
    products = Products.objects.filter(category__name='Backend')
    context = {
        'title': 'Backend Development',
        'products': products,
    }
    return render(request, 'goods/backend.html', context)


def frontend(request):
    products = Products.objects.filter(category__name='Frontend')
    context = {
        'title': 'Frontend Development',
        'products': products,
    }
    return render(request, 'goods/frontend.html', context)

def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product,
    }
    return render(request, 'goods/admissions.html', context)

def search(request):
    goods = q_search(request)

    context = {
        'title': 'Search Results',
        'products': goods,
    }
    return render(request, 'goods/frontend.html', context)