from django.urls import path
from . import views

urlpatterns = [
    # URLs para proyectos
    path('projects/', views.getProjects, name='get_projects'),
    path('projects/add/', views.addProject, name='add_project'),
    path('projects/update/<int:project_id>/', views.updateProject, name='update_project'),
    path('projects/delete/<int:project_id>/', views.deleteProject, name='delete_project'),
    path('projects/<int:project_id>/', views.getProjectDetail, name='project_detail'),
    path('projects/with-appointments/', views.getProjectsWithAppointments, name='projects_with_appointments'),

    # URLs para clientes
    path('clients/', views.getClients, name='get_clients'),
    path('clients/add/', views.addClient, name='add_client'),
    path('clients/update/<int:client_id>/', views.updateClient, name='update_client'),
    path('clients/delete/<int:client_id>/', views.deleteClient, name='delete_client'),
    path('clients/<int:client_id>/', views.getClientDetail, name='client_detail'),

    # URLs para citas (appointments)
    path('appointments/', views.getAppointments, name='get_appointments'),
    path('appointments/add/', views.addAppointment, name='add_appointment'),
    path('appointments/update/<int:appointment_id>/', views.updateAppointment, name='update_appointment'),
    path('appointments/delete/<int:appointment_id>/', views.deleteAppointment, name='delete_appointment'),
    path('appointments/<int:appointment_id>/', views.getAppointmentDetail, name='appointment_detail'),
]
