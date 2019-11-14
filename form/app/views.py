#conding:utf-8
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import Autn
# Create your views here.

class Regist(View):
    TEMPLATE = 'regist.html'
    def get(self,request):
        form = Autn()
        return render(request,self.TEMPLATE,{'form':form})

    def post(self,request):

       form = Autn(request.POST)
       if form.is_valid():

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        print(username,password)
       return redirect('/regist')
