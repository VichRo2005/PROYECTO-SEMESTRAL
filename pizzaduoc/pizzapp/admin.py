from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Comuna, DetallePedido, EstadoPedido, Pedido, PreguntasFrecuentes, Productos, TipoProducto, TipoUsuario, Usuario

admin.site.register(Comuna)
admin.site.register(DetallePedido)
admin.site.register(EstadoPedido)
admin.site.register(Pedido)
admin.site.register(PreguntasFrecuentes)
admin.site.register(Productos)
admin.site.register(TipoProducto)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)