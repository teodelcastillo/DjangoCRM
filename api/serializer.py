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
        # Obtén el nombre del cliente asociado al proyecto
        return project.client.name
        
class ClientSerializer (serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class AppointmentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class ProjectWithAppointmentsSerializer(ProjectSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)
