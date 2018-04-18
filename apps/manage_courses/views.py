from django.shortcuts import render, HttpResponse

def index(request):
    print "It works"
    return render(request, "manage_courses/index.html")

def create(request):
    return HttpResponse('We created')

def remove(request, id):
    print id
    return HttpResponse(id)

def destroy(request, id):
    print id
    return HttpResponse(id)
