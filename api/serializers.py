from rest_framework import serializers
from DjangoProjectManager.models import Client, Project

class ClientSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Client
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"