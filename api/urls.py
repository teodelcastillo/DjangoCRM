from django.urls import path
from . import views

urlpatterns = [

    ### Clients ###
    path('clients/', views.getClients),
    path('newClient/', views.addClient),
    path('clients/<int:client_id>/', views.getClientDetail),
    path('updateClient/<int:client_id>/', views.addClient),
    path('deleteClient/<int:client_id>/', views.deleteClient),
    path('clients/<int:pk>/projects/', views.client_projects),

    ### Projects ###
    path('projects/', views.getProjects),
    path('newProject/', views.addProject),
    path('updateProject/<int:project_id>/', views.updateProject),
    path('deleteProject/<int:project_id>/', views.deleteProject),
    path('projects/<int:project_id>/', views.getProjectDetail),
    path('projectsWithAppointments/', views.getProjectsWithAppointments, name='projects-with-appointments'),

    ### Appointments ###
    path('appointments/', views.getAppointments),
    path('newAppointment/', views.addAppointment),
    path('updateAppointment/<int:appointment_id>/', views.updateAppointment),
    path('deleteAppointment/<int:appointment_id>/', views.deleteAppointment),
    path('appointments/<int:appointment_id>/', views.getAppointmentDetail),
]
