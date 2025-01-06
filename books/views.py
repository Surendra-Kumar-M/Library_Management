from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *
from rest_framework import status,generics,permissions
from rest_framework.decorators import api_view

# Create your views here.

class ReactView(APIView):
    serializer_class = ReactSerializer

    

    def get(self,request):
        books=Books.objects.all()
        serializer=self.serializer_class(books,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=ReactSerializer(data=request)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


    
    




