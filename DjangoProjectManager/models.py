from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    # Información básica del cliente
    name = models.CharField(max_length=100)
    clientID = models.CharField(max_length=11, unique=True)
    assignedTo = models.ManyToManyField(User, related_name='assigned_clients', default=User.objects.get(username='teodorodelcastillo').id)

    def __str__(self):
        return (f"{self.name} - {self.clientID}")

class Project(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name= 'projects')
    projectName = models.CharField(max_length=150)
    projectId = models.CharField(max_length=20, unique=True, blank=True)
    projectDescription = models.TextField(default='Completar informacion')
    projectStatus = models.CharField(max_length=20, choices=(('Active', 'Active'), ('Finished', 'Finished')), default='Active')
    projectFolderNumber = models.CharField(max_length=5, blank=True)
    projectLink = models.CharField(max_length=1000, default='adelcastillo.com.ar')
    projectJury = models.CharField(max_length=200, blank=True)
    assignedTo = models.ManyToManyField(User, related_name='assigned_projects', default=User.objects.get(username='teodorodelcastillo').id)

    def __str__(self):
        return f"{self.projectName} - {self.projectId}"

class Contact(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='contacts')
    contactName = models.CharField(max_length=50)
    contactPhone = models.CharField(max_length=20)
    contactEmail = models.CharField(max_length=100)
    contactRole = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.contactName} - {self.contactEmail}")

class Appointment(models.Model):

    # Campos específicos del Appointment
    title = models.TextField(default='pruebas')
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()

    # Campos para el estado de la cita
    is_done = models.BooleanField(default=False)
    done_date = models.DateTimeField(null=True, blank=True)
    done_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    done_comment = models.TextField(null=True, blank=True)

    # Relación con Client (opcional, si un Appointment está relacionado a un Cliente)
    client = models.ForeignKey(Client, on_delete=models.CASCADE,
                               null=True, blank=True, related_name='appointments')

    # Relación con Project (opcional, si un Appointment está relacionado a un Proyecto)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='appointments')
    
    assignedTo = models.ManyToManyField(User, related_name='assigned_appointments', default=User.objects.get(username='teodorodelcastillo').id)

    @property
    def client(self):
        return self.project.client if self.project else None

    def __str__(self):
        return f"Appointment on {self.date} at {self.time}"

