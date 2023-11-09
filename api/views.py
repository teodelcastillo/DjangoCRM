from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from django.contrib.auth.models import User
from DjangoProjectManager.models import Client, Project, Appointment
from .serializer import UserSerializer, ClientSerializer, ProjectSerializer, AppointmentSerializer, ProjectWithAppointmentsSerializer

class CustomPageNumberPagination(PageNumberPagination):
    page_size: 10

### PROJECTS ###

# Get projects (GET)
@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()

    paginator = CustomPageNumberPagination()
    result_page = paginator.paginate_queryset(projects, request)

    serializer = ProjectSerializer(result_page, many=True)
    return Response(serializer.data)


# Add a new project (POST)
@api_view(['POST'])
def addProject(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update client by ID (PUT)
@api_view(['PUT'])
def updateProject(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProjectSerializer(project, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete project by ID (DELETE)
@api_view(['DELETE'])
def deleteProject(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    project.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Get project by ID (GET)
@api_view(['GET'])
def getProjectDetail(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProjectSerializer(project)
    return Response(serializer.data)


# Get projects with appointments (GET)
@api_view(['GET'])
def getProjectsWithAppointments(request):
    projects = Project.objects.filter(appointments__isnull=False).distinct()
    serializer = ProjectWithAppointmentsSerializer(projects, many=True)
    return Response(serializer.data)

# Get projects with appointments not done (GET)
@api_view(['GET'])
def getUncompletedProjects(request):
    projects = Project.objects.filter(appointments__is_done=False).distinct()

    paginator = CustomPageNumberPagination()
    result_page = paginator.paginate_queryset(projects, request)

    serializer = ClientSerializer(result_page, many=True)
    return Response(serializer.data)


### CLIENTS ###

# Get clients (GET)
@api_view(['GET'])
def getClients(request):
    clients = Client.objects.all()

    paginator = CustomPageNumberPagination()
    result_page = paginator.paginate_queryset(clients, request)

    serializer = ClientSerializer(result_page, many=True)
    return Response(serializer.data)

# Add a new client (POST)
@api_view(['POST'])
def addClient(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update client by ID (PUT)
@api_view(['PUT'])
def updateClient(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ClientSerializer(client, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete client by ID (DELETE)
@api_view(['DELETE'])
def deleteClient(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    client.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Get client by ID (GET)
@api_view(['GET'])
def getClientDetail(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ClientSerializer(client)
    return Response(serializer.data)


### APPOINTMENTS ###

# Get appointments (GET)
@api_view(['GET'])
def getAppointments(request):
    appointments = Appointment.objects.all()

    paginator = CustomPageNumberPagination()
    result_page = paginator.paginate_queryset(appointments, request)

    serializer = AppointmentSerializer(result_page, many=True)
    return Response(serializer.data)

# Add a new appointment (POST)
@api_view(['POST'])
def addAppointment(request):
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update appointment by ID (PUT)
@api_view(['PUT'])
def updateAppointment(request, appointment_id):
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
    except Appointment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = AppointmentSerializer(appointment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete appointment by ID (DELETE)
@api_view(['DELETE'])
def deleteAppointment(request, appointment_id):
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
    except Appointment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    appointment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Get appointment by ID (GET)
@api_view(['GET'])
def getAppointmentDetail(request, appointment_id):
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
    except Appointment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = AppointmentSerializer(appointment)
    return Response(serializer.data)


### Users ###

@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()

    paginator = CustomPageNumberPagination()
    result_page = paginator.paginate_queryset(users, request)

    serializer = UserSerializer(result_page, many=True)
    return Response(serializer.data)