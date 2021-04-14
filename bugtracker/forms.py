from django.forms import ModelForm
from . import models


class ProjectForm(ModelForm):
    class Meta:
        model = models.Project
        fields = '__all__'


class BugForm(ModelForm):
    class Meta:
        model = models.Bug
        fields = '__all__'
