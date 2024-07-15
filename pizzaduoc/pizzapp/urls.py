from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

#para logins
from django.contrib.auth import views as auth_views

urlpatterns = [

     path('main.html', views.index, name='main'),
     path('carrito.html' , views.carrito, name='carrito'),
     path('CARTA.html' , views.CARTA, name='carta'),
     path('historial.html' , views.historial, name='historial'),
     path('PREGUNTAS.html', views.preguntas_frecuentes, name='PREGUNTAS'),
     path('registro.html' , views.registro, name='registro'),
     path('AdminPage.html' , views.AdminPage, name='AdminPage'),
     path('CARTA_COMPLETA.html' , views.CARTA_COMPLETA, name='carta_completa'),
     path('agregar_al_pedido/<int:pedido_id>/<int:producto_id>/', views.agregar_al_pedido, name='add'),
     path('eliminar_del_pedido/<int:pedido_id>/<int:producto_id>/', views.eliminar_del_pedido, name='del'),
     path('usuariosAdd', views.usuariosAdd, name='usuariosAdd'),
     path('login' , auth_views.LoginView.as_view(), name= 'login'),
     path('logout', auth_views.LogoutView.as_view(), name='logout_user'),
     path('', views.bienvenido, name='bienvenido')
]
