from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    nombre = models.CharField(max_length=50, default=None)
    apellido = models.CharField(max_length=50, default=None)
    telefono = models.CharField(max_length=15, default=None)
    mail = models.EmailField(default=None)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre

class Deposito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Deposito'
        verbose_name_plural = 'Depositos'
    
    def __str__(self):
        return str(self.producto)

class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto_venta = models.ManyToManyField(Producto, through='ProductosCarrito')
    vendido = models.BooleanField()

    class Meta:
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'

    def __str__(self):
        return str(self.id)

    @property
    def get_monto_carrito (self):
        productos = self.productoscarrito_set.all()
        total = sum([item.get_total for item in productos]) 
        return total

    @property
    def get_items_carrito (self):
        productos = self.productoscarrito_set.all()
        total = sum([item.cant_prod for item in productos]) 
        return total    
    

class ProductosCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cant_prod = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Productos en Carrito'
        verbose_name_plural = 'Productos en Carritos'

    def __str__(self):
        return str(self.cant_prod)

    @property
    def get_total(self):
        total = self.producto.precio * self.cant_prod
        return total

class Venta(models.Model):
    metodos_de_pago = [
        ('transferencia', 'transferencia'),
        ('debito', 'debito'),
        ('credito', 'credito'),
    ]
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    productoscarrito = models.ForeignKey(ProductosCarrito, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=50, choices=metodos_de_pago, default=None)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return str(self.carrito)