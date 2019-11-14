#coding:utf-8
from django import template
register = template.Library() #定义过滤器

@register.filter
def test(value,args):
    return value*args