from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PostSerializer
from .models import Postm

@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        a=serializer.save()
        if a==serializer:
            return Response("Already exist")
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def read_product(request):
    Data=Postm.objects.all()
    Data=PostSerializer(Data,many=True)
    return Response(Data.data)
