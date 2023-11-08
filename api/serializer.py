from rest_framework import serializers
from django.contrib.auth.models import User
from DjangoProjectManager.models import Project, Client, Appointment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        
class ProjectSerializer(serializers.ModelSerializer):
    clientName = serializers.SerializerMethodField()  # Agrega el campo 'clientName'

    class Meta:
        model = Project
        fields = '__all__'

    def get_clientName(self, project):
        
        return project.client.name
        
class ClientSerializer(serializers.ModelSerializer):
    ammount_of_projects = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = '__all__'

    def get_ammount_of_projects(self, client):
        return client.ammount_of_projects()

class AppointmentSerializer (serializers.ModelSerializer):
    projectName = serializers.SerializerMethodField()
    clientName = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = '__all__'
    
    def get_projectName(self, appointment):
        return appointment.project.projectName
    
    def get_clientName(self, appointment):
        return appointment.client.name


class ProjectWithAppointmentsSerializer(ProjectSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)
