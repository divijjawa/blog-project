from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
authors =[
    {'author' : 'divij_jawa',
    'content' : 'blog_div',
    'title' :'hello123',
    'date_posted':'12 april 2019'},

    {'author' : 'Joe',
    'content' : 'abc',
    'title' :'help',
    'date_posted':'10 april 2019'}
]

def blog_home(request):
    context ={
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def blog_about(request):
    return render(request,'blog/about.html',{'title':'About Page'})