from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),

    # Projects
    path('view_project/<int:pk>/', views.view_project, name='project'),
    path('delete_project/<int:pk>/', views.delete_project, name='delete_project'),
    path('add_project/', views.add_project, name='add_project'),
    path('update_project/<int:pk>/', views.update_project, name='update_project'),

    # Clients
    path('clients/', views.clients, name='clients'),
    path('add_client/', views.add_client, name='add_client'),
    path('view_client/<int:pk>/', views.view_client, name='view_client'),
    path('delete_client/<int:pk>/', views.delete_client, name='delete_client'),
    path('update_client/<int:pk>/', views.update_client, name='update_client'),
    path('client/<int:pk>/projects/',
         views.client_projects, name='client_projects'),


    # Appointments
    path('appointments/', views.appointments, name='appointments'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('update_appointment/<int:pk>/',
         views.update_appointment, name='update_appointment'),
    path('delete_appointment/<int:pk>/',
         views.delete_appointment, name='delete_appointment'),
    path('view_appointment/<int:pk>/',
         views.view_appointment, name='view_appointment'),
]
