#from django.shortcuts import render
#from django.http import JsonResponse
from .models import Category
from .serializers import * 
from rest_framework import viewsets
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = []

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = []

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []

class DepositViewSet(viewsets.ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
    permission_classes = []

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = []

class ProductsCartViewSet(viewsets.ModelViewSet):
    queryset = ProductsCart.objects.all()
    serializer_class = ProductsCartSerializer
    permission_classes = []

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = []


# class SupplierViewSet(viewsets.ModelViewSet):
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierSerializer
#     permission_classes = []
