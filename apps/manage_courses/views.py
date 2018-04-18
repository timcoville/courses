from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

def index(request):
    context = { 'courses': Course.objects.all()}
    return render(request, "manage_courses/index.html", context)

def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            print tag + ": " + error
        return redirect('/')
    else:
        Course.objects.create(name=request.POST['name'],desc=request.POST['desc'])
    return redirect('/')

def remove(request, id):
    print id
    return HttpResponse(id)

def destroy(request, id):
    print id
    return HttpResponse(id)
