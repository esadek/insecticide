from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Bug(models.Model):
    STATUS = [
        ('Open', 'Open'),
        ('In progress', 'In progress'),
        ('To be tested', 'To be tested'),
        ('Reopen', 'Reopen'),
        ('Closed', 'Closed')
    ]
    PRIORITY = [
        ('High', 'High'),
        ('Normal', 'Normal'),
        ('Low', 'Low')
    ]
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='Open')
    priority = models.CharField(max_length=10, choices=PRIORITY, default='Normal')
    creation_date = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return self.name
