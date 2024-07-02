from django.urls import path
from .import views

urlpatterns = [

    path('main.html', views.index, name='main'),
     path('blank.html' , views.blank, name='blank'),
     path('carrito.html' , views.carrito, name='carrito'),
     path('CARTA.html' , views.CARTA, name='CARTA'),
     path('ejemplos.html' , views.ejemplos, name='ejemplos'),
     path('historial.html' , views.historial, name='historial'),
     path('ingresar.html' , views.ingresar, name= 'ingresar'),
     path('PREGUNTAS.html' , views.PREGUNTAS, name='PREGUNTAS'),
     path('registro.html' , views.registro, name='registro'),
     path('AdminPage.html' , views.AdminPage, name='AdminPage'),
]