from rest_framework import serializers
from DjangoProjectManager.models import Project, Client, Appointment

class ProjectSerializer (serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

        
class ClientSerializer (serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class AppointmentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

