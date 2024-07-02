from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("你好. You're at the polls index.")
