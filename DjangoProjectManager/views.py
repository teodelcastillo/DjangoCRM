from .models import Client  # Import your Client model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Project, Client, Appointment
from .forms import ProjectForm, ClientForm, AppointmentForm


def home(request):
    projects = Project.objects.all()

    # Check to see if logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')
        else:
            messages.success(request, 'Error logging in. Please try again.')
            return redirect('home')
    else:
        return render(request, 'home.html', {'projects': projects})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')

# Projects


def view_project(request, pk):
    if request.user.is_authenticated:

        project = Project.objects.get(id=pk)
        return render(request, 'project.html', {'project': project})

    else:
        messages.success(request, 'You must be logged in to view that.')
        return redirect('home')


def delete_project(request, pk):
    if request.user.is_authenticated:
        delete_it = Project.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Project deleted.')
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in to do that.')
        return redirect('home')


def add_project(request):
    form = ProjectForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_project = form.save()
                messages.success(request, 'Project added.')
                return redirect('home')
        return render(request, 'add_project.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to do that.')
        return redirect('home')


def update_project(request, pk):
    if request.user.is_authenticated:
        current_project = Project.objects.get(id=pk)
        form = ProjectForm(request.POST or None, instance=current_project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated.')
            return redirect('home')
        return render(request, 'update_project.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to do that.')
        return redirect('home')

# Clients


def clients(request):

    clients = Client.objects.all()

    if request.user.is_authenticated:
        return render(request, 'clients.html', {'clients': clients})
    else:
        messages.success(request, 'You must be logged in to do that.')
        return redirect('home')


def add_client(request):
    form = ClientForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_client = form.save()
                messages.success(request, 'Client added.')
                return redirect('clients')
        return render(request, 'add_client.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to do that.')
        return redirect('home')


def view_client(request, pk):
    if request.user.is_authenticated:

        client = Client.objects.get(id=pk)
        return render(request, 'view_client.html', {'client': client})

    else:
        messages.success(request, 'You must be logged in to view that.')
        return redirect('home')


def delete_client(request, pk):
    if request.user.is_authenticated:
        delete_it = Client.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Client deleted.')
        return redirect('clients')
    else:
        messages.success(request, 'You must be logged in to do that.')
        return redirect('home')


def update_client(request, pk):
    if request.user.is_authenticated:
        current_client = Client.objects.get(id=pk)
        form = ClientForm(request.POST or None, instance=current_client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client updated.')
            return redirect('clients')
        return render(request, 'update_client.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to do that.')
        return redirect('home')


def client_projects(request, pk):
    if request.user.is_authenticated:
        client = Client.objects.get(pk=pk)  # Use 'pk' to retrieve the client
        projects = client.projects.all()  # Access projects using the related name
        return render(request, 'client_projects.html', {'client': client, 'projects': projects})
    else:
        messages.success(request, 'You must be logged in to view that.')
        return redirect('home')


# Appointments


def appointments(request):

    appointments = Appointment.objects.all()

    if request.user.is_authenticated:
        return render(request, 'appointments.html', {'appointments': appointments})
    else:
        messages.success(request, 'You must be logged in to do that.')
        return redirect('home')


def add_appointment(request):
    form = AppointmentForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_appointment = form.save()
                messages.success(request, 'Appointment added.')
                return redirect('appointments')
        return render(request, 'add_appointment.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to do that.')
        return redirect('home')


def update_appointment(request, pk):
    if request.user.is_authenticated:
        current_appointment = Appointment.objects.get(id=pk)
        form = AppointmentForm(request.POST or None,
                               instance=current_appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment updated.')
            return redirect('appointments')
        return render(request, 'update_appointment.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to do that.')
        return redirect('home')


def view_appointment(request, pk):
    if request.user.is_authenticated:

        appointment = Appointment.objects.get(id=pk)
        return render(request, 'view_appointment.html', {'appointment': appointment})
    else:
        messages.success(request, 'You must be logged in to view that.')
        return redirect('home')


def delete_appointment(request, pk):
    if request.user.is_authenticated:

        delete_it = Appointment.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Appointment deleted.')
        return redirect('appointments')
    else:
        messages.success(request, 'You must be logged in to do that.')
        return redirect('home')


def project_appointments(request, pk):
    if request.user.is_authenticated:
        # Use 'pk' to retrieve the project
        project = Project.objects.get(pk=pk)
        # Access appointments using the related name
        appointments = project.appointments.all()
        return render(request, 'project_appointments.html', {'project': project, 'appointments': appointments})
    else:
        messages.success(request, 'You must be logged in to view that.')
        return redirect('home')
