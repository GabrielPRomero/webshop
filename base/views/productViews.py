from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers

from django.contrib.auth.models import User
import rest_framework
from base.models import Product
from base.serializer import ProductSerializer, UserSerializer, UserSerializerWithToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status


@api_view(['GET'])
def getProducts(request):
    query = request.query_params.get('keyword')

    if query == None:
        query = ''

    products = Product.objects.filter(name__icontains=query)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createProduct(request):

    user = request.user

    product = Product.objects.create(user=user,
                                     name='Name',
                                     price=0,
                                     brand='Brand',
                                     countInStock=0,
                                     category="Category",
                                     description="Description")
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateProduct(request, pk):
    data = request.data
    product = Product.objects.get(_id=pk)

    product.name = data['name']
    product.price = data['price']
    product.brand = data['brand']
    product.countInStock = data['countInStock']
    product.category = data['category']
    product.description = data['description']

    product.save()

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def uploadImage(req):
    data = req.data

    product_id = data['product_id']
    product = Product.objects.get(_id=product_id)

    product.image = req.FILES.get('image')
    product.save()

    return Response('upload successful')
