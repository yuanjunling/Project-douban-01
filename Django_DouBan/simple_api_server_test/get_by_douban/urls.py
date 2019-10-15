#coding:utf-8
from django.urls import path
from .views import Music,Movie
urlpatterns = [
    path('music/',Music.as_view()),
    path('movie/',Movie.as_view())
]