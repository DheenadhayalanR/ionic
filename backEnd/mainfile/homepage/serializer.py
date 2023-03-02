from rest_framework import serializers
from .models import Postm

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postm
        fields = '__all__'
