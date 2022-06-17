from django.shortcuts import render
from django.http import httpresponse
# Create your views here.
def first (request):
    return httpresponse('<h1><marquee>this is our first FBV</marquee></h1>')
    def second(request):
        return httpresponse('second FBV')