from django.urls import path
from . import views

urlpatterns = [
    path('getClients/', views.getData),
    path('addClient/', views.addClient)
]
