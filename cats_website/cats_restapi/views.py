from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.views import APIView, Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Cat
from .serializers import CatSerializer

# Create your views here.

class CatsListView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CatSerializer
    def get_queryset(self):
        user = self.request.user
        return user.cats.all()
    

class CatsDetailView(RetrieveUpdateDestroyAPIView):  
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CatSerializer

    def get_queryset(self):
        user = self.request.user
        return user.cats.all()
