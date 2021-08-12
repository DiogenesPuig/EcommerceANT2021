#from django.shortcuts import render
#from django.http import JsonResponse
from .models import *
from .serializers import * 
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser
#from rest_framework.response import Response
#from rest_framework.decorators import action


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
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

    # @action(detail=True,methods=['post', 'put'])
    # def add_to_cart(self, request, pk=None):
    #     cart = self.get_object()
    #     try:
    #         product = Product.objects.get(pk=request.data['product_id'])
    #         quantity = int(request.data['cant_prod'])
    #     except Exception as e:
    #         print (e)
    #         return Response({'status': 'fail'})

    #     existing_cart_item = ProductsCart.objects.filter(cart=cart,product=product).first()

    #     if existing_cart_item:
    #         existing_cart_item.quantity += quantity
    #         existing_cart_item.save()
    #     else:
    #         new_cart_item = ProductsCart(cart=cart, product=product, cant_prod=quantity)
    #         new_cart_item.save()

    #     serializer = CartSerializer(cart)
    #     return Response(serializer.data)

class ProductsCartViewSet(viewsets.ModelViewSet):
    queryset = ProductsCart.objects.all()
    serializer_class = ProductsCartSerializer
    permission_classes = []

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = []

class RegisterView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]