from django.db import models
from django.utils import timezone

# Create your models here.
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=255)
    description = models.TextField()
    hours = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
