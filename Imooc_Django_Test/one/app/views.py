from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View

class Index(View):
    def get(self,request,name,age):
        return HttpResponse('hello i am {0},age is{1}'.format(name,age))

