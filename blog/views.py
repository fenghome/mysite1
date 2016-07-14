# coding:utf-8
from django.http.response import HttpResponse
from django.shortcuts import render
from blog.controller.Houtai.Index.IndexController import IndexController

from blog.models import Users


def admin(request,a,c):
    obj = IndexController()
    return obj.run()

def blog(request):
    return render(request,'Blog/index.html')

def login(request):
    return render(request,'houtai/login.html')


def head(request):
    user = Users.objects.get(userid = '1')
    return render(request, 'houtai/head.html',{"user":user})
#
# def left(request):
#     return render(request, 'houtai/left.html')
#
# def right(request):
#     return render(request, 'houtai/right.html')
#
# def showUser(request):
#     return render(request, 'houtai/showUser.html')
#
# def showColumn(request):
#     return render(request, 'houtai/showColumn.html')
#
# def showArticles(request):
#     return render(request, 'houtai/showArticles.html')
#
# def addUser(request):
#     return render(request, 'houtai/addUser.html')
#
# def editPass(request):
#     return render(request, 'houtai/editPass.html')
#
# def addColumn(request):
#     return render(request, 'houtai/addColumn.html')
#
# def addArticle(request):
#     return render(request, 'houtai/addArticle.html')
#
# def editUser(request):
#     return render(request, 'houtai/editUser.html')
#
# def editColumn(request):
#     return render(request, 'houtai/editColumn.html')
#
# def editArticle(request):
#     return render(request, 'houtai/editArticle.html')
