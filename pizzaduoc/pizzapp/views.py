from django.shortcuts import render, redirect
from .models import Comuna, DetallePedido, EstadoPedido, Pedido, PreguntasFrecuentes, Productos, TipoProducto, Usuario
import requests  #ESTE ES PARA LA API,NO CONFUNDIR CON REQUEST DE DJANGO
from datetime import date, datetime
from django.db import connection
import math
from django.contrib import messages
from .globals import idUsuario

# imports para sistema Login
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#import para registrar
from django.contrib.auth.models import User
#import para autenticación
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

V_idUsuario = idUsuario

#registration
def usuariosAdd(request):
      #Es un POST, por lo tanto se recuperan los datos del formulario y se graban en la tabla
      nombre=request.POST["nombre"]
      apellido_paterno=request.POST["apellido_paterno"]
      mail=request.POST["mail"]
      clave=request.POST["clave"]
      telefono=request.POST["telefono"]
      v_username = nombre[0:3] + "" + apellido_paterno[0:3] + "" + telefono[0:3]

      v_direccion = "default"
      obj=User.objects.create(             
            username = v_username,
            first_name = nombre,
            last_name = apellido_paterno,
            email = mail,
            password = clave,
            is_staff = False,
            is_active = True,
            is_superuser = False,
            )
      obj.save()
      newobj=Usuario.objects.create(             
            user = User.objects.get(username=v_username),
            telefono = telefono,
            direccion = v_direccion,
            comuna_id_comuna = Comuna.objects.get(id_comuna=1),
            )
      newobj.save()

      context={'mensaje':"Datos guardados, inicie sesión para continuar..."}
      return render(request, 'pizzapp/registro.html', context)

#login
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): 
            cd = form.cleaned_data
            user = authenticate(request,
                                username = cd['username'],
                                password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Usuario Autenticado')
                else:  
                    return HttpResponse('Usuario no activo')
            else:
                return HttpResponse('Información incorrecta')
    else:
        form = LoginForm()
        return render(request, 'registration/login', {'form': form})

def index(request):
    context={}
    return render(request, 'pizzapp/main.html', context)

def bienvenido(request):
    context={}
    return render(request, 'pizzapp/bienvenido.html', context)
    
def logout_user(request):
        return render(request, '')
    
def registro(request):
    context={}
    return render(request, 'pizzapp/registro.html', context)

#VISTA HISTORIAL-----------------------------------------
@login_required
def historial(request):

    query = request.GET.get('busqueda', '')
    if query:
        pedidos = Pedido.objects.select_related('estado_pedido_id_estado').filter(fecha_pedido__icontains=query)
    else:
        pedidos = Pedido.objects.select_related('estado_pedido_id_estado').all()
    return render(request, 'Pizzapp/historial.html', {'pedidos': pedidos})

@login_required
@staff_member_required
def AdminPage(request):
    return render(request, 'pizzapp/AdminPage.html')


#Vista filtrar preguntas-------------------------------------------
def preguntas_frecuentes(request):
    query = request.GET.get('busqueda', '')
    if query:
        preguntas = PreguntasFrecuentes.objects.filter(pregunta__icontains=query)
    else:
        preguntas = PreguntasFrecuentes.objects.all()
    return render(request, 'Pizzapp/PREGUNTAS.html', {'preguntas': preguntas})


#==============================PROGRAMACION LOGICA DEL CARRITO==========================================================
def CARTA(request): #esto va en el lado de views
    current_user = request.user
    variable = current_user.id
    print(variable)

    pedido_actual = Pedido()
    pedido_actual.setear_cliente(variable) #esta solicitud se hace al backend, no muestra nada
    idpedido = Pedido.objects.raw("SELECT COUNT(*) as id_pedido FROM pedido;") #aca ahora se asigna el id de pedido correspondiente
    # hacer query para mostrar solo los primeros 8 productos
    productos = Productos.objects.raw("SELECT * FROM productos where id_producto <=8")
    return render(request, 'pizzapp/CARTA.html', {'productos': productos, 'idpedido': idpedido})
	
def CARTA_COMPLETA(request): #este va en el lado de views
#hacer query para mostrar todos los productos.
    idpedido = Pedido.objects.raw("SELECT COUNT(*) as id_pedido FROM pedido;") #aca ahora se asigna el id de pedido correspondiente
    productos = Productos.objects.raw("SELECT * FROM productos")
    return render(request, 'pizzapp/CARTA_COMPLETA.html', {'productos': productos, 'idpedido': idpedido})	

def agregar_al_pedido(request, pedido_id, producto_id):
    # Obtener el pedido existente
    pedido = Pedido.objects.get(id_pedido=pedido_id)
    # Obtener la instancia del modelo Productos correspondiente al ID proporcionado
    producto = Productos.objects.get(id_producto=producto_id)    

    # Encontrar el último detalle para este pedido
    last_detalle = DetallePedido.objects.filter(pedido_id_pedido=pedido).order_by('-seq_pedido').first()

    # Calcular la siguiente secuencia
    next_seq = last_detalle.seq_pedido + 1 if last_detalle else 1

    # Crear un nuevo DetallePedido con la secuencia incrementada y la instancia del producto
    nuevo_detalle = DetallePedido(pedido_id_pedido=pedido, seq_pedido=next_seq, productos_id_producto=producto)
    nuevo_detalle.save()

    return render(request, 'pizzapp/CARTA.html', {'pedido': pedido})  # Reemplaza 'tu_plantilla.html' con el nombre de tu plantilla

def eliminar_del_pedido(request, pedido_id, producto_id):
    # Obtener el pedido existente
    pedido = Pedido.objects.get(id_pedido=pedido_id)
    # Buscar el último DetallePedido relacionado con el producto específico
    detalle_a_eliminar = DetallePedido.objects.filter(pedido_id_pedido=pedido, productos_id_producto=producto_id).last()
    if detalle_a_eliminar is not None:
        detalle_a_eliminar.delete()
        messages.success(request, 'El producto se eliminó del pedido.')
    else:
        messages.error(request, 'No se encontró ningún detalle para eliminar.')
        return render(request, 'pizzapp/CARTA.html', {'pedido': pedido})
    
    return render(request, 'pizzapp/CARTA.html', {'pedido': pedido, 'messages': messages.get_messages(request)})
        

def carrito(request):
    query_idpedido = "SELECT COUNT(*) as id_pedido FROM pedido;"

    locacion_pizzeria = "Sta. Elena de Huechuraba 1660, 8600036 Huechuraba, Región Metropolitana"
    fee_delivery = 500
    
    with connection.cursor() as cursor:
          
          cursor.execute(query_idpedido)
          idpedido = cursor.fetchone()
          v_idpedido = int(''.join(map(str, idpedido)))

          cursor.execute("SELECT direccion ||', '|| c.descripcion_comuna FROM usuario u INNER JOIN comuna c on u.comuna_id_comuna = c.id_comuna WHERE u.user_id = %s", [V_idUsuario])

          ubicacion_cliente = cursor.fetchone()
          v_ubicacion_cliente = str(''.join(map(str, ubicacion_cliente)))
          url= f"https://api.distancematrix.ai/maps/api/distancematrix/json?origins={locacion_pizzeria}&destinations={v_ubicacion_cliente}&key=i6FZLB3QCz2gUscSTGXNogkRWj7wfzK56YP84kEMsmLa1kEgig3ttCeZoiemrWu6"
          response = requests.get(url)
          data = response.json()
          distancia = data['rows'][0]['elements'][0]['distance']['text']	
          distancia_km = math.trunc(float(distancia.split()[0]))# Extrae el valor numérico
          valor_delivery = fee_delivery * distancia_km


          cursor.execute("SELECT SUM(p.precio_oferta) FROM detalle_pedido dp INNER JOIN productos p ON p.id_producto = dp.productos_id_producto WHERE pedido_id_pedido = %s", [v_idpedido])
          total = cursor.fetchone()
          v_total = int(''.join(map(str, total)))

          v_total_general = valor_delivery + v_total

          cursor.execute("UPDATE pedido SET total = %s WHERE id_pedido = %s", [v_total_general, v_idpedido]) #actualizacion del total, para mostrarlo en carrito.html

          cursor.execute("SELECT id_pedido, usuario_id_usuario, total FROM pedido WHERE id_pedido = %s", [v_idpedido])
          pedido = cursor.fetchone()

          cursor.execute("SELECT p.desc_corta FROM detalle_pedido dt INNER JOIN productos p ON p.id_producto = dt.productos_id_producto WHERE dt.pedido_id_pedido = %s", [v_idpedido])
          detallepedido = cursor.fetchall()

          print('Pedido:', pedido)
          print('Detalle Pedido:', detallepedido)

    return render(request, 'pizzapp/carrito.html', {'pedido': pedido, 'detallepedido': detallepedido})