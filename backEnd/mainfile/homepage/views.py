from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PostSerializer
from .models import Details

@api_view(['POST'])
def create_product(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        a=serializer.save()
        if a==serializer:
            return Response("Already exist")
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def read_product(request):
    Data=Details.objects.all()
    Data=PostSerializer(Data,many=True)
    return Response(Data.data)

@api_view(['PUT'])
def update_product(request,pk):
    Data=Details.objects.get(id=pk)
    serializer=PostSerializer(instance=Data,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_product(request,pk):
    Data=Details.objects.get(id=pk)
    Data.delete()
    return Response("Deleted")
