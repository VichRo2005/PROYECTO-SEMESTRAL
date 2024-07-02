from django.db import models
from .globals import idUsuario
from datetime import date, datetime
import math
from django.db import connections
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


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

    def setear_cliente(self):
        v_idpedido = Pedido.objects.raw("SELECT COUNT(*) + 1 FROM pizzapp_pedido")
        v_fecha_pedido = date.today().strftime("%d/%m/%Y")
        v_hora_pedido = datetime.now().strftime("%H:%M")
        v_total = 0
        v_estadopedido = 1
        v_usuario = idUsuario
        with connections.cursor() as cursor:
            cursor.execute("INSERT INTO pedido (id_pedido, fecha_pedido, hora_pedido, total, estado_pedido_id_estado, usuario_id_usuario VALUES (%s, %s, %s, %s, %s, %s)", [v_idpedido, v_fecha_pedido, v_hora_pedido, v_total, v_estadopedido, v_usuario])


    def calcular_pedido(self, p_idPedido):
        total_pedido = DetallePedido.objects.raw("SELECT SUM(p.precio_oferta) FROM pizzap_detalle_pedido dp INNER JOIN pizzapp_productos p ON p.id_producto = dp.productos_id_producto WHERE pedido_id_pedido = %s", [p_idPedido])
        return total_pedido


    def calcular_delivery(self, p_idUsuario):
        feeDelivery = 500
        direccionPizzeria = "Sta. Elena de Huechuraba 1660, 8600036 Huechuraba, Región Metropolitana"
        direccionCliente = Usuario.objects.raw("SELECT direccion ||', '|| c.descripcion_comuna FROM pizzapp_usuario u INNER JOIN pizzapp_comuna c on u.comuna_id_comuna = c.id_comuna WHERE u.id_usuario = %s", [p_idUsuario])
        dirCliExact = direccionCliente + ", Region Metropolitana"
        url= f"https://api.distancematrix.ai/maps/api/distancematrix/json?origins={direccionPizzeria}&destinations={dirCliExact}&key=i6FZLB3QCz2gUscSTGXNogkRWj7wfzK56YP84kEMsmLa1kEgig3ttCeZoiemrWu6"
        response = requests.get(url)
        data = response.json()
        distancia = data['rows'][0]['elements'][0]['distance']['text']	
        distancia_km = math.trunc(float(distancia['text'].split()[0]) ) # Extrae el valor numérico
        valor_delivery = feeDelivery * distancia_km
        
        return valor_delivery



    def calcular_total(self):
        v_usuario = idUsuario
        v_idpedido = Pedido.objects.raw("SELECT COUNT(*) FROM pizzapp_pedido")
        delivery = calcular_delivery(v_usuario)
        pedido = calcular_pedido(v_idpedido)
        total = (delivery + pedido)
        with connections.cursor() as cursor:
            cursor.execute("UPDATE pedido SET total = %s WHERE id_pedido = %s", [total, v_idpedido])   





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
    path_imagen = models.CharField(max_length=20, blank=True, null=True)
    tipo_producto_seq_tipproduct = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='tipo_producto_seq_tipproduct')

    class Meta:

        db_table = 'productos'


class TipoProducto(models.Model):
    seq_tipproduct = models.BigIntegerField(primary_key=True)
    desc_tip_producto = models.CharField(max_length=150)

    class Meta:

        db_table = 'tipo_producto'


class TipoUsuario(models.Model):
    id_tipo_usuario = models.BigIntegerField(primary_key=True)
    desc_tip_usuario = models.CharField(max_length=100)

    class Meta:

        db_table = 'tipo_usuario'


class Usuario(models.Model):
    id_usuario = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50, blank=True, null=True)
    mail = models.CharField(max_length=50)
    clave = models.CharField(max_length=10)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=100)
    estado_usuario = models.FloatField()
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_id_comuna')
    tipo_usuario_id_tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='tipo_usuario_id_tipo_usuario')

    class Meta:

        db_table = 'usuario'

