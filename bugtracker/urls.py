from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:id>/', views.project, name='project'),
    path('bugs/', views.bugs, name='bugs'),
    path('bug/<int:id>/', views.bug, name='bug')
]
