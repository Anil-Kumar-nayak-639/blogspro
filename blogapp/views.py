from django.shortcuts import render,redirect
from mysql import connector as sql
from blogapp.models import post
from django.contrib.auth.decorators import login_required
# Create your views here.

def page(request):
    return render(request,'page.html')

def home(request):
    obj = post.objects.all()
    return render (request,'home.html',{'obj':obj})

def singlepost(request,url):
    obj=post.objects.filter(url=url)

    return render (request,'singlepost.html',{'obj':obj})

def addpost(request):

    if request.method == "POST":
        p=post()
        p.title = request.POST.get('title')
        p.content = request.POST.get('content')
        p.url = request.POST.get('url')
        p.image = request.FILES['img']
        p.name = request.POST.get('uname')
        p.save()
    return render (request,'post.html')

def delete_post(request,id):
    obj = post.objects.get(pk=id)
    obj.delete()
    return redirect ('home')