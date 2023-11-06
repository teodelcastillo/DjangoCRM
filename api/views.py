from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from DjangoProjectManager.models import Client, Project, Appointment
from .serializer import ClientSerializer, ProjectSerializer, AppointmentSerializer

### PROJECTS ###

# Get projects (GET)
@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many = True)
    data = serializer.data

    for project in data:
        clientId = project['client']
        client = Client.objects.get(pk = clientId)
        project['clientName'] = client.name

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
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)
