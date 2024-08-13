from django.shortcuts import render
from goods.models import Categories, Products

# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def courses(request):

    categories = Categories.objects.all()


    context = {
        'title': 'Choose Your Side!',
        'categories': categories,
    }
    return render(request, 'main/courses.html', context)


def backend(request):
    products = Products.objects.filter(category__name='Backend')
    context = {
        'title': 'Backend Development',
        'products': products,
    }
    return render(request, 'main/backend.html', context)
