#coding:utf-8
from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50,blank=False,unique=True)
    age = models.SmallIntegerField(default=0)
    phone = models.IntegerField(db_index=True,blank=True,default=0,max_length=11)
    email = models.EmailField(blank=True,default='',unique=True)
    info = models.TextField(max_length=500)
    create_time = models.DateTimeField(auto_now_add=True)
    updata_time = models.DateTimeField(auto_now=True)

class Userprofile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.SET_NULL)
    birthday = models.CharField(max_length=100,blank=True,default='')
class Diary(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User,related_name='diary',on_delete=models.SET_NULL,blank=True,null=True)
    content = models.TextField()