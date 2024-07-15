from django.db import models
from .globals import idUsuario
from datetime import date, datetime
import math
from django.db import connection
import requests
from django.conf import settings

from django.contrib.auth.models import User



class Comuna(models.Model):
    id_comuna = models.BigIntegerField(primary_key=True)
    descripcion_comuna = models.CharField(max_length=150)

    class Meta:
        db_table = 'comuna'


class DetallePedido(models.Model):
    pedido_id_pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='pedido_id_pedido')
    seq_pedido = models.BigIntegerField(primary_key=True)  # Establecer como clave primaria
    productos_id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='productos_id_producto')

    class Meta:
        db_table = 'detalle_pedido'
        unique_together = (('pedido_id_pedido', 'seq_pedido'),)


class EstadoPedido(models.Model):
    id_estado = models.BigIntegerField(primary_key=True)
    descripcion_estado = models.CharField(max_length=30)

    class Meta:

        db_table = 'estado_pedido'


class Pedido(models.Model):
    id_pedido = models.BigIntegerField(primary_key=True)
    fecha_pedido = models.CharField(max_length=10)
    hora_pedido = models.CharField(max_length=6)
    total = models.BigIntegerField(blank=True, null=True)
    estado_pedido_id_estado = models.ForeignKey(EstadoPedido, models.DO_NOTHING, db_column='estado_pedido_id_estado')
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_id_usuario')

    class Meta:

        db_table = 'pedido'

    def setear_cliente(self, variable):
        query = "SELECT COUNT(*) + 1 as id_pedido FROM pedido;"
        with connection.cursor() as cursor:
            cursor.execute(query)
            idpedido = cursor.fetchone()
            v_idpedido = int(''.join(map(str, idpedido)))
            

            v_fecha_pedido = date.today().strftime("%d/%m/%Y")
            v_hora_pedido = datetime.now().strftime("%H:%M")
            v_total = 0
            v_estadopedido = 1
            cursor.execute("INSERT INTO pedido (id_pedido, fecha_pedido, hora_pedido, total, estado_pedido_id_estado, usuario_id_usuario) VALUES (%s, %s, %s, %s, %s, %s)", [v_idpedido, v_fecha_pedido, v_hora_pedido, v_total, v_estadopedido, variable])
"""
    def calcular_pedido(self):
        total_pedido = self.total.extra(
            select={'total': 'SUM(productos.precio_oferta)'},
            tables=['detalle_pedido', 'productos'],
            where=['detalle_pedido.productos_id_producto = productos.id_producto']
        ).values('total').first()
        return total_pedido['total'] or 0
 

    def calcular_delivery(self):
        feeDelivery = 500
        direccionPizzeria = "Sta. Elena de Huechuraba 1660, 8600036 Huechuraba, Región Metropolitana"
        direccionCliente = Usuario.objects.raw("SELECT u.id_usuario, direccion ||', '|| c.descripcion_comuna FROM usuario u INNER JOIN comuna c on u.comuna_id_comuna = c.id_comuna WHERE u.id_usuario = %s", [p_idUsuario])
        dirCliExact = direccionCliente[0].direccion + ", " + direccionCliente[0].comuna_id_comuna.descripcion_comuna + ", Región Metropolitana"
        url= f"https://api.distancematrix.ai/maps/api/distancematrix/json?origins={direccionPizzeria}&destinations={dirCliExact}&key=i6FZLB3QCz2gUscSTGXNogkRWj7wfzK56YP84kEMsmLa1kEgig3ttCeZoiemrWu6"
        response = requests.get(url)
        data = response.json()
        distancia = data['rows'][0]['elements'][0]['distance']['text']	
        distancia_km = math.trunc(float(distancia.split()[0]))# Extrae el valor numérico
        valor_delivery = feeDelivery * distancia_km
        
        return valor_delivery



    def calcular_total(self):
        delivery = self.calcular_delivery()
        total_pedido = self.calcular_pedido()
        total = delivery + total_pedido
        self.total = total
        self.save()
        return total
"""




class PreguntasFrecuentes(models.Model):
    id_pregunta = models.BigIntegerField(primary_key=True)
    pregunta = models.CharField(max_length=200)
    respuesta = models.CharField(max_length=200)

    class Meta:

        db_table = 'preguntas_frecuentes'
    


class Productos(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    desc_corta = models.CharField(max_length=100)
    desc_larga = models.CharField(max_length=200)
    precio_real = models.BigIntegerField()
    precio_oferta = models.BigIntegerField(blank=True, null=True)
    path_imagen = models.ImageField(upload_to= "img/")
    tipo_producto_seq_tipproduct = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='tipo_producto_seq_tipproduct')

    class Meta:

        db_table = 'productos'


class TipoProducto(models.Model):
    seq_tipproduct = models.BigIntegerField(primary_key=True)
    desc_tip_producto = models.CharField(max_length=150)

    class Meta:

        db_table = 'tipo_producto'



class Usuario(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=100)
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, default=999, db_column='comuna_id_comuna')
 
    class Meta:

        db_table = 'usuario'

