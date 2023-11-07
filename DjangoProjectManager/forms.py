from django import forms
from .models import Project, Client, Appointment


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"
