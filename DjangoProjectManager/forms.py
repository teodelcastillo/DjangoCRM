from django import forms
from .models import Project, Client, Appointment


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'client',
            'projectName',
            'projectId',
            'projectDescription',
            'projectStatus',
            'projectFolderNumber',
            'projectLink',
            'projectJury',
        ]

    # Cambia el campo client a un ModelChoiceField
    client = forms.ModelChoiceField(
        queryset=Client.objects.all(),
        empty_label=None,  # Elimina la opción vacía
        label="Cliente"  # Cambia el etiquetado del campo
    )


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"
