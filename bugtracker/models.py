from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)


class Bug(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    creation_date = models.DateField()
    due_date = models.DateField()
