from django.contrib import admin
from ECommerce.models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','category','supplier')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','tel', 'email' )

    fieldsets = (
        ('Datos Personales', {
            'fields' : ('user','first_name', 'last_name')
        }),
        ('Contacto', {
            'fields' : ('tel', 'email')
        })
    )

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel')

class CartAdmin(admin.ModelAdmin):
    list_display = ('id','get_items_cart','get_monto_cart','sold')

class SaleAdmin(admin.ModelAdmin):
    list_display = ('id','cart', 'payment_method','date')

class ProductCartAdmin(admin.ModelAdmin):
    list_display = ('cart','product','cant_prod','get_total')

class DepositAdmin(admin.ModelAdmin):
    list_display = ('product','stock')


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Category)
admin.site.register(Deposit,DepositAdmin)
admin.site.register(ProductsCart,ProductCartAdmin)
