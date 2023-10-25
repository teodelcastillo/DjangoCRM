from rest_framework.response import Response
from rest_framework.decorators import api_view
from DjangoProjectManager.models import Client
from .serializers import ClientSerializer

@api_view(['GET'])
def getData(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many= True)
    return Response(serializer.data)

