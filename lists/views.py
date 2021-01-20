from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def lists_main(request):
    return HttpResponse("hi", status=200)
