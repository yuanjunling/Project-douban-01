#coding:utf-8
from django.urls import path
from .views import TestOne

urlpatterns = [
    path('TestOne/<str:message>',TestOne.as_view(),name='TestOne')
]