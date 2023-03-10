from django.urls import path
from homepage.views import create_product,read_product

urlpatterns = [
    path('create/', create_product, name='create_product'),
     path('read/', read_product, name='read_product'),
]
