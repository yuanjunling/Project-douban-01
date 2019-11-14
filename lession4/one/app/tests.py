from django.test import TestCase

# Create your tests here.
from .models import Userprofile,Diary
import time
diary = Diary.objects.create(user=user,content='hahahahha',create_time=time.time())