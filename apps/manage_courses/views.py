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
    return render(request, "manage_courses/confirm.html", context = {'course': Course.objects.get(id = id)})

def destroy(request, id):
    Course.objects.get(id = id).delete()
    return redirect('/')
