from django.shortcuts import render,HttpResponse
from .models import *
from django.http import *
from .forms import *
# def index(request):
#     b=books.objects.all()
#     for i in b:
#         print(i.title)
#         print(i.pages)
#         print(i.created_by)
#         print('---------------------')
#     return HttpResponse('hello')
# Create your views here.
def index(request):
    d=books.objects.all()
    return render(request,'home.html',{'info':d})

def authorform(request):
    if request.method=="POST":
        form=author_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=author_form()
    return render(request,'author.html',{"form":form})
def bookform(request):
    if request.method=="POST":
        form = book_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=book_form()
    return render(request,'book.html',{"form":form})