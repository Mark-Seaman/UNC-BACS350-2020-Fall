from django.contrib import admin
from django.urls import path

from page.views import index, HomePage


urlpatterns = [
    path('', index),
    path('home', HomePage.as_view()),
    
]
