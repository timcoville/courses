from django.shortcuts import render, HttpResponse

def index(request):
    print "It works"
    return HttpResponse('It works')


