from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from . import views

app_name = 'goods'

urlpatterns = [
    path('', views.courses, name='courses'),
    path('backend', views.backend, name='backend'),
    path('frontend', views.frontend, name='frontend'),
    path("product/<slug:product_slug>/", views.product, name='product'),
    path("search/", views.search, name='search'),
]


