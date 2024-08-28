from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #Queda relacionado a la clase Proyect, on_delete = Que borre la tarea al eliminarse el Proyecto

# python manage.py shell
# Python 3.10.9 (main, Jul 11 2024, 15:54:57) [GCC 13.2.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from myapp.models import Project, Task           
# >>> Project.objects.get(id=1)
# <Project: Project object (1)>
# >>> p = Project.objects.get(id=1)
# >>> p.task_set.all()
# <QuerySet []>
# >>> p.task_set.create(title="Descargar IDE")
# <Task: Task object (1)>
# >>> p.task_set.all()
# <QuerySet [<Task: Task object (1)>]>
# >>> p.task_set.create(title="Desarrollar login")
# <Task: Task object (2)>
# >>> p.task_set.get(id=1)
# <Task: Task object (1)>
# >>> Project.objects.filter(name__startswith="aplicacion")
# <QuerySet [<Project: Project object (1)>, <Project: Project object (2)>]>
# >>> Project.objects.filter(name__startswith="abc")
# <QuerySet []>