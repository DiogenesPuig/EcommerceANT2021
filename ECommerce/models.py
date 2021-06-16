from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50, default=None)
    apellido = models.CharField(max_length=50, default=None)
    telefono = models.CharField(max_length=15, default=None)
    mail = models.EmailField(default=None)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return "Nombre: " + self.nombre + "tel: " + self.telefono

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Deposito(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return self.product

class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto_venta = models.ManyToManyField(Producto, through='ProductosCarrito')
    monto_total = models.IntegerField(default=0)
    vendido = models.BooleanField()

    def __str__(self):
        return self.producto_venta.__str__()

class ProductosCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cant_prod = models.IntegerField()

    def __str__(self):
        return str(self.cant_prod)

class Venta(models.Model):
    metodos_de_pago = [
        ('transferencia', 'transferencia'),
        ('debito', 'debito'),
        ('credito', 'credito'),
    ]
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    fecha = models.DateField()
    metodo_pago = models.CharField(max_length=50, choices=metodos_de_pago, default=None)
    precio_final = models.IntegerField(default=None)

    def __str__(self):
        return self.carrito