from django.urls import path
from homepage.views import create_post

urlpatterns = [
    path('api/posts/', create_post, name='create_post'),
]
