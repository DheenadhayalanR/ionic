from django.urls import path
from homepage.views import items

urlpatterns = [
    path('create/', items.create_product, name='create_product'),
    path('read/', items.read_product, name='read_product'),
    path('read/<int:pk>',items.readid_product, name='readid_product'),
    path('update/<int:pk>', items.update_product, name='update_product'),
    path('delete/', items.delete_product, name='delete_product'),
]
