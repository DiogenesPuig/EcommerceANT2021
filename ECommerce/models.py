from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50,default=None)
    apellido = models.CharField(max_length=50,default=None)
    telefono = models.CharField(max_length=15, default=None)
    mail = models.EmailField(default=None)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

class Producto(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

 #---------------------------------hace producto compra

class Deposito(models.Model):
    product = models.ForeignKey(Producto,on_delete=models.CASCADE)
    stock = models.IntegerField()

class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    producto_venta = models.ManyToManyField(Producto, through='ProductosCarrito')
    monto_total = models.IntegerField(default=0)
    vendido = models.BooleanField()

class ProductosCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cant_prod = models.IntegerField()


class Venta(models.Model):
    metodos_de_pago = [
        ('transferencia', 'transferencia'),
        ('debito', 'debito'),
        ('credito', 'credito'),
    ]
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    fecha = models.DateField()
    metodo_pago = models.CharField(max_length=50,choices= metodos_de_pago ,default=None)
    precio_final = models.IntegerField(default=None)
