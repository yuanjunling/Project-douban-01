from django.test import TestCase
import requests
# Create your tests here.
url = 'http://127.0.0.1:8000/music'
data = {'musicname':'红色高跟鞋'}

response = requests.get(url,params=data)

rs = response.json()
print(rs)