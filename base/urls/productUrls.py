from django.urls import path
from django.urls.resolvers import URLPattern
from base.views import productViews as views

urlpatterns = [
    path('', view=views.getProducts, name="products"),
    path('create/', view=views.createProduct, name="createProduct"),
    path('upload/', view=views.uploadImage, name="uploadProductImage"),
    path('<str:pk>/', view=views.getProduct, name="product"),
    path('update/<str:pk>/', view=views.updateProduct, name="UpdateProduct"),
]
