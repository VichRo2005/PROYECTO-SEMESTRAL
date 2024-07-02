
from django.shortcuts import render, redirect
from .models import Comuna, DetallePedido, EstadoPedido, Pedido, PreguntasFrecuentes, Productos, TipoProducto, TipoUsuario, Usuario
import requests  #ESTE ES PARA LA API,NO CONFUNDIR CON REQUEST DE DJANGO
from datetime import date, datetime
from django.db import connections
import math
# Create your views here.
idUsuario = 1; #este dejarlo como variable goblal

def index(request):
    context={}
    return render(request, 'pizzapp/main.html', context)

def blank(request):
    context={}
    return render(request, 'pizzapp/blank.html', context)


def ejemplos(request):
    context={}
    return render(request, 'pizzapp/ejemplos.html', context)

def historial(request):
    context={}
    return render(request, 'pizzapp/historial.html', context)

def ingresar(request):
    context={}
    return render(request, 'pizzapp/ingresar.html', context)

def registro(request):
    context={}
    return render(request, 'pizzapp/registro.html', context)

def PREGUNTAS(request):
    context={}
    return render(request, 'pizzapp/PREGUNTAS.html', context)

def AdminPage(request):
    context={}
    return render(request, 'pizzapp/AdminPage.html', context)

#==============================PROGRAMACION LOGICA DEL CARRITO==========================================================
def CARTA(request): #esto va en el lado de views
#hacer query para mostrar solo los primeros 8 productos
	productos = Productos.objects.raw("SELECT * FROM pizzapp_productos where id_producto <=8")
	return render(request, 'pizzapp/CARTA.html', {'productos': productos})
	
def CARTA_COMPLETA(request): #este va en el lado de views
#hacer query para mostrar todos los productos.
	productos = Productos.objects.raw("SELECT * FROM pizzapp_productos")
	return render(request, 'pizzapp/CARTA_COMPLETA.html', {'productos': productos})	

def agregar_al_pedido(request, pedido_id, producto_id):
    # Obtener el pedido existente
    pedido = Pedido.objects.get(id_pedido=pedido_id)

    # Encontrar el último detalle para este pedido
    last_detalle = DetallePedido.objects.filter(pedido_id_pedido=pedido).order_by('-seq_pedido').first()

    # Calcular la siguiente secuencia
    next_seq = last_detalle.seq_pedido + 1 if last_detalle else 1

    # Crear un nuevo DetallePedido con la secuencia incrementada
    nuevo_detalle = DetallePedido(pedido_id_pedido=pedido, seq_pedido=next_seq, productos_id_producto=producto_id)
    nuevo_detalle.save()

def eliminar_del_pedido(request, pedido_id, producto_id):
    # Obtener el pedido existente
    pedido = Pedido.objects.get(id_pedido=pedido_id)
    # Buscar el último DetallePedido relacionado con el producto específico
    detalle_a_eliminar = DetallePedido.objects.filter(pedido_id_pedido=pedido, productos_id_producto=producto_id).last()
    detalle_a_eliminar.delete()

def carrito(request):
    v_idpedido = Pedido.objects.raw("SELECT COUNT(*) FROM pizzapp_pedido")   
    pedido_actual = Pedido.objects.get(id_pedido=v_idpedido)
    pedido_actual.calcular_total()
    pedido = Pedido.objects.raw("SELECT id_pedido, total FROM pizzapp_pedido WHERE id_pedido = %s", [v_idpedido])
    detallepedido = DetallePedido.objects.raw("SELECT p.desc_corta FROM pizzapp_detalle_pedido dt INNER JOIN pizzapp_productos p ON p.id_producto = dt.productos_id_producto WHERE dt.pedido_id_pedido =%s", [v_idpedido])
    return render(request, 'pizzapp/carrito.html', {'pedido':pedido, 'detallepedido':detallepedido})