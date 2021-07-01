from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from model_utils import FieldTracker

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=50, default=None)
    last_name = models.CharField(max_length=50, default=None)
    tel = models.CharField(max_length=15, default=None)
    email = models.EmailField(default=None)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.first_name

class Supplier(models.Model):
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

class Deposit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Deposit'
        verbose_name_plural = 'Deposits'
    
    def __str__(self):
        return str(self.product)

class Cart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_sale = models.ManyToManyField(Product, through='ProductsCart')
    sold = models.BooleanField()
    tracker = FieldTracker()

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return str(self.id)

    @property
    def get_monto_cart (self):
        products = self.product_in_cart_set.all()  #idk q es esto
        total = sum([item.get_total for item in products])
        return total

    @property
    def get_items_cart (self):
        products = self.product_in_cart_set.all()
        total = sum([item.cant_prod for item in products])
        return total    
    

class ProductsCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    cant_prod = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Productos en Carrito'
        verbose_name_plural = 'Productos en Carritos'

    def __str__(self):
        return str(self.cant_prod)

    @property
    def get_total(self):
        total = self.product.price * self.cant_prod
        return total

class Sale(models.Model):
    payment_methods = [
        ('transferencia', 'transferencia'),
        ('debito', 'debito'),
        ('credito', 'credito'),
    ]
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_in_cart = models.ForeignKey(ProductsCart, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=payment_methods, default=None)

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'

    def __str__(self):
        return str(self.cart)

@receiver(post_save, sender=Cart)
def update_stock(sender, instance, created, **kwargs):
    if not created:
        if instance.vendido:
            previus_sale = instance.tracker.previous('vendido')
            new_sale = instance.vendido
            if previus_sale != new_sale:
                prod_carrito = ProductsCart.objects.filter(carrito = instance)
                if(prod_carrito.count() > 0):
                    for item in prod_carrito:
                        product = Product.objects.get(id = item.producto.id)
                        prod_stock = Deposit.objects.filter(producto = product)
                        for deposit in prod_stock:
                            deposit.stock -= item.cant_prod
                            deposit.save()