from django.db import models


class Bug(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    creation_date = models.DateField()
    due_date = models.DateField()
