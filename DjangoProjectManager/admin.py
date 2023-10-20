from django.contrib import admin
from .models import Client, Contact, Project, Appointment

admin.site.register(Client)
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(Appointment)
