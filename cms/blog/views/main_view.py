
from django.shortcuts import render,redirect
from ..models import Blogs


def home(request):
    return render(request,'main/home.html')  


def single_blog(request):
    return render(request,'main/single_blog.html')

def edit_blog(request):
    return render(request,'main/edit_blog.html')


def create_blog(request):
    if request.method=="POST":
        title=request.POST.get("title")
        subtitle=request.POST.get("subtitle")
        desc=request.POST.get("desc")
        blog=Blogs(title=title,subtitle=subtitle,description=desc)
        blog.save()
        return redirect("register")

    return render(request,'main/create_blog.html')