from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('courses', views.courses, name='courses')
]
