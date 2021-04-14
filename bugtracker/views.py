from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models, forms


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def projects(request):
    projects = models.Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects.html', context)

def project(request, id):
    project = models.Project.objects.get(id=id)
    context = {'project': project}
    return render(request, 'project.html', context)

def create_project(request):
    if request.method == 'POST':
        form = forms.ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = forms.ProjectForm()
    context = {'form': form}
    return render(request, 'form.html', context)

def bugs(request):
    bugs = models.Bug.objects.all()
    context = {'bugs': bugs}
    return render(request, 'bugs.html', context)

def bug(request, id):
    bug = models.Bug.objects.get(id=id)
    context = {'bug': bug}
    return render(request, 'bug.html', context)

def create_bug(request):
    if request.method == 'POST':
        form = forms.BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bugs')
    else:
        form = forms.BugForm()
    context = {'form': form}
    return render(request, 'form.html', context)
