from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #Queda relacionado a la clase Proyect, on_delete = Que borre la tarea al eliminarse el Proyecto
