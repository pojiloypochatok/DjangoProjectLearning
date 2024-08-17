from django.shortcuts import render
from goods.models import Categories, Products


# Create your views here.

def index(request):
    return render(request, 'main/index.html')



