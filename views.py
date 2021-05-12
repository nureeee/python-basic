from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<body bgcolor=ffffff text=red> 오늘은 수요일입니다. <br><hr>')
