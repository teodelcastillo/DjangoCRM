from django.contrib import admin
from .models import Appointment, Project, Client

admin.site.register(Appointment)
admin.site.register(Project)
admin.site.register(Client)