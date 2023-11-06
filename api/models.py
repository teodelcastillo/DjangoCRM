
from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    # Información básica del cliente
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    clientID = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return (f"{self.name} - {self.clientID}")


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


class Project(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    projectName = models.CharField(max_length=150)
    projectId = models.CharField(max_length=20, unique=True)
    projectDescription = models.TextField(blank=False)
    projectStatus = models.CharField(max_length=20, default="Active")
    projectFolderNumber = models.CharField(max_length=5)
    projectLink = models.CharField(max_length=1000)
    projectJury = models.CharField(max_length=200)
    assignedTo = models.ManyToManyField(User, related_name='projects', default= "Teodoro del Castillo")

    def __str__(self):
        return (f"{self.projectName} - {self.projectId}")


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
    client = models.ForeignKey(Client, on_delete=models.SET_NULL,
                               null=True, blank=True, related_name='appointments')

    # Relación con Project (opcional, si un Appointment está relacionado a un Proyecto)
    project = models.ForeignKey(
        Project, on_delete=models.SET_NULL, null=True, blank=True, related_name='appointments')

    def __str__(self):
        return f"Appointment on {self.date} at {self.time}"
