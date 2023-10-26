from django.urls import path
from . import views

urlpatterns = [

    ### Clients ###
    path('getClients/', views.getClients),
    path('addClient/', views.addClient),
    path('getClientDetail/<int:client_id>/', views.getClientDetail),
    path('updateClient/<int:client_id>/', views.addClient),
    path('deleteClient/<int:client_id>/', views.deleteClient),
    path('client/<int:pk>/projects/', views.client_projects),

    ### Projects ###
    path('getProjects/', views.getProjects),
    path('addClient/', views.addProject),
    path('updateProject/<int:project_id>/', views.updateProject),
    path('deleteProject/<int:project_id>/', views.deleteProject),
    path('getProjectDetails/<int:project_id>/', views.getProjectDetail),
]
