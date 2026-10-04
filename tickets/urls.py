from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tickets, name='lista_tickets'),
    path('nuevo/', views.crear_ticket, name='crear_ticket'),
    path('<int:pk>/editar/', views.editar_ticket, name='editar_ticket'),
]