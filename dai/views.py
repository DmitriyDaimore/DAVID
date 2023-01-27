from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("хоть по китайски, <<H1>> для машини без разницы какой символ")
