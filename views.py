from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    s=" <h1>registration form </h1>"
    res=render(request,'registrationform/register_template.html')
    return res
