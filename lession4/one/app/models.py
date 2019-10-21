#coding:utf-8
from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50,blank=False,unique=True)
    age = models.SmallIntegerField(default=0)
    phone = models.SmallIntegerField(db_index=True,blank=True,default=0)
    email = models.EmailField(blank=True,default='',unique=True)
    info = models.TextField(max_length=500)
    create_time = models.DateTimeField(auto_now_add=True)
    updata_time = models.DateTimeField(auto_now=True)
