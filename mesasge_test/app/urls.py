#coding:utf-8
from django.urls import path
from .views import TestOne

urlpatterns = [
    path('TestOne/<str:message_type>',TestOne.as_view(),name='three')
]