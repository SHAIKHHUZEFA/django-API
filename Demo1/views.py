from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Demo
from .serializers import BookSerializer
from rest_framework import status

# Create your views here.
class info(APIView):
    def get(self,request):
        data1=Demo.objects.all()
        seri1=BookSerializer(data1,many=True)
        return Response(seri1.data)

    def Post(self,request):
         detail=BookSerializer(data=request.data)
         if detail.is_valid():
             detail.save()
             return Response(detail.data,status=status.HTTP_200_OK)