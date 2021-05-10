from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('projects/', views.projects, name='projects'),
    path('project/create/', views.create_project, name='create project'),
    path('project/<int:id>/', views.project, name='project'),
    path('bugs/', views.bugs, name='bugs'),
    path('bug/create/', views.create_bug, name='create bug'),
    path('bug/<int:id>/', views.bug, name='bug'),
]
