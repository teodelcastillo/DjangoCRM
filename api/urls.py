from django.urls import path
from . import views

urlpatterns = [
    path('getClients/', views.getData),
    path('addClient/', views.addClient),
    path('getClientDetail/<int:client_id>/', views.getData),
    path('updateClient/<int:client_id>/', views.addClient),
    path('deleteClient/<int:client_id>/', views.addClient)
]
