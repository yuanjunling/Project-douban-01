#coding:utf-8
from django.shortcuts import render
import datetime
from jinja2 import environment
from django.contrib.staticfiles.storage import staticfiles_storage
# Create your views here.
from django.views.generic import View

class Index(View):
    TEMPLATE = 'index.html'
    def get(self,request,name):
        data = {}
        data['name'] =name
        data['array'] = range(10)
        data['count'] = 20
        data['time'] = datetime.datetime.now()
        return render(request,self.TEMPLATE,data)