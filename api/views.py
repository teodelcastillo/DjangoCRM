from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from DjangoProjectManager.models import Client
from .serializers import ClientSerializer

@api_view(['GET'])
def getData(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many= True)
    return Response(serializer.data)

@api_view(['POST'])
def addClient(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Código 201 para indicar que se ha creado el recurso
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Manejar errores de validación

