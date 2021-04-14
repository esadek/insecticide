from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Bug


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects.html', context)

def project(request, id):
    project = Project.objects.get(id=id)
    context = {'project': project}
    return render(request, 'project.html', context)

def bugs(request):
    bugs = Bug.objects.all()
    context = {'bugs': bugs}
    return render(request, 'bugs.html', context)
