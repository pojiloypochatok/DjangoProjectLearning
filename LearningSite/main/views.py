from django.shortcuts import render



# Create your views here.

def index(request):
    context ={
        'title': 'Home Page'
    }
    return render(request, 'main/index.html')



