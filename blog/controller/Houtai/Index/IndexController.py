# coding:utf-8
from django.shortcuts import render_to_response

__author__ = 'Administrator'
class IndexController:
    def run(self):
        return render_to_response('Houtai/index/index.html')