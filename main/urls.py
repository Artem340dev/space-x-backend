from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('elements/create', views.createWebsiteElement),
    path('elements/all', views.getAllElements),
    path('elements/get', views.getElement),
    path('elements/save', views.saveElements)
]