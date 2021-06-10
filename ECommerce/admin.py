from django.contrib import admin
from ECommerce.models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio','categoria','proveedor')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','telefono', 'mail' )

    fieldsets = (
        ('Datos Personales', {
            'fields' : ('nombre', 'apellido')
        }),
        ('Contacto', {
            'fields' : ('telefono', 'mail')
        })
    )

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono')

class CarritoAdmin(admin.ModelAdmin):
    list_display = ('cliente',)

class VentaAdmin(admin.ModelAdmin):
    list_display = ('carrito', 'metodo_pago','fecha')




# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Categoria)
admin.site.register(Deposito)
