from rest_framework import serializers
from DjangoProjectManager.models import Client, Project, Appointment

class ClientSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Client
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    clientName = serializers.CharField(source='client.name', read_only = True)

    class Meta:
        model = Project
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"

class ProjectWithAppointmentsSerializer(ProjectSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)
