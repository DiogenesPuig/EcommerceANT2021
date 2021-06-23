from django.contrib import admin
from ECommerce.models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio','categoria','proveedor')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','telefono', 'mail' )

    fieldsets = (
        ('Datos Personales', {
            'fields' : ('user','nombre', 'apellido')
        }),
        ('Contacto', {
            'fields' : ('telefono', 'mail')
        })
    )

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono')

class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id','cliente','get_items_carrito','get_monto_carrito','vendido')

class VentaAdmin(admin.ModelAdmin):
    list_display = ('id','carrito', 'metodo_pago','fecha')

class ProductosCarritoAdmin(admin.ModelAdmin):
    list_display = ('cant_prod','get_total')

class DepositoAdmin(admin.ModelAdmin):
    list_display = ('producto','stock')


# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Categoria)
admin.site.register(Deposito,DepositoAdmin)
admin.site.register(ProductosCarrito,ProductosCarritoAdmin)
