from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from . import models, forms


def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'signup.html', context)


@login_required
def dashboard(request):
    context = {}
    context['latest_bugs'] = models.Bug.objects.all().order_by('-id')[:6]
    context['total_count'] = models.Bug.objects.all().count()
    context['open_count'] = models.Bug.objects.filter(status='Open').count()
    context['in_progress_count'] = models.Bug.objects.filter(status='In progress').count()
    context['to_be_tested_count'] = models.Bug.objects.filter(status='To be tested').count()
    context['closed_count'] = models.Bug.objects.filter(status='Closed').count()
    context['reopen_count'] = models.Bug.objects.filter(status='Reopen').count()
    context['high_count'] = models.Bug.objects.filter(priority='High').count()
    context['normal_count'] = models.Bug.objects.filter(priority='Normal').count()
    context['low_count'] = models.Bug.objects.filter(priority='Low').count()
    return render(request, 'dashboard.html', context)


@login_required
def projects(request):
    projects = models.Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects.html', context)


@login_required
def project(request, id):
    project = models.Project.objects.get(id=id)
    form = forms.ProjectForm(instance=project)
    if request.method == 'POST':
        form = forms.ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'form.html', context)


@login_required
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


@login_required
def bugs(request):
    bugs = models.Bug.objects.all()
    context = {'bugs': bugs}
    return render(request, 'bugs.html', context)


@login_required
def bug(request, id):
    bug = models.Bug.objects.get(id=id)
    form = forms.BugForm(instance=bug)
    if request.method == 'POST':
        form = forms.BugForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('bugs')
    context = {'form': form}
    return render(request, 'form.html', context)


@login_required
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
