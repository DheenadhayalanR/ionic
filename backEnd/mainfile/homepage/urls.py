from django.urls import path
from homepage.views import create_post,read_product

urlpatterns = [
    path('create/', create_post, name='create_post'),
     path('read/', read_product, name='read_product'),
]
