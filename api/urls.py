from django.urls import path
from . import views

urlpatterns = [
    path('getClients/', views.getClients),
    path('addClient/', views.addClient),
    path('getClientDetail/<int:client_id>/', views.getClientDetail),
    path('updateClient/<int:client_id>/', views.addClient),
    path('deleteClient/<int:client_id>/', views.deleteClient),
    path('client/<int:pk>/projects/', views.client_projects),
]
