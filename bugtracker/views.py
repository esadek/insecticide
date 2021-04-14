from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def projects(request):
    projects = models.Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects.html', context)

def project(request, id):
    project = models.Project.objects.get(id=id)
    context = {'project': project}
    return render(request, 'project.html', context)

def bugs(request):
    bugs = models.Bug.objects.all()
    context = {'bugs': bugs}
    return render(request, 'bugs.html', context)

def bug(request, id):
    bug = models.Bug.objects.get(id=id)
    context = {'bug': bug}
    return render(request, 'bug.html', context)
