from rest_framework import serializers
from django.contrib.auth.models import User
from DjangoProjectManager.models import Project, Client, Appointment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        
class ClientSerializer(serializers.ModelSerializer):
    amount_of_projects = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = '__all__'

    def get_amount_of_projects(self, client):
        return client.projects.count()


class ProjectSerializer(serializers.ModelSerializer):
    clientName = serializers.SerializerMethodField()
    amount_of_appointments = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_clientName(self, project):
        return project.client.name
    
    def get_amount_of_appointments(self, project):
        return project.client.projects.count() 


class AppointmentSerializer (serializers.ModelSerializer):
    project_name = serializers.SerializerMethodField()
    client_name = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = '__all__'
    
    def get_project_name(self, appointment):
        return appointment.project.projectName
    
    def get_client_name(self, appointment):
        return appointment.client.name


class ProjectWithAppointmentsSerializer(ProjectSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)

