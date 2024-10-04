from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest
from django.core.exceptions import ValidationError

from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_spectacular.utils import extend_schema
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.openapi import OpenApiParameter, OpenApiExample

from .models import Breed, Cat, CatRating
from .serializers import CatSerializer, BreedSerializer, UserSerializer, CatRatingsSerializer


@extend_schema(request={
    'application/x-www-form-urlencoded': {
        'type': 'object',
        'properties': {
            'name': {
                'type': 'string',
                'description': 'Name of the cat'
            },
            'breed': {
                'type': 'string',
                'description': 'Name of the breed',
                'enum': Breed.objects.values_list('name', flat=True)
            },
            'age': {
                'type': 'integer',
                'description': 'Age in full months'
            },
            'color': {
                'type': 'string'
            },
            'description': {
                'type': 'string'
            },
        },
        'required': ['name', 'breed', 'age', 'color', 'description'],
    },
    'application/json': {
        'type': 'object',
        'properties': {
            'name': {
                'type': 'string',
                'description': 'Name of the cat'
            },
            'breed': {
                'type': 'string',
                'description': 'Name of the breed',
                'enum': Breed.objects.values_list('name', flat=True),
            },
            'age': {
                'type': 'integer'
            },
            'color': {
                'type': 'string'
            },
            'description': {
                'type': 'string'
            },
        },
        'required': ['name', 'breed', 'age', 'color', 'description'],
    },
}, )
class CatsListView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CatSerializer

    def get_queryset(self):
        user = self.request.query_params.get('owner_name')
        breed_name = self.request.query_params.get('breed')
        if breed_name and user:
            return Cat.objects.filter(breed__name=breed_name, owner__username=user)
        elif breed_name:
            return Cat.objects.filter(breed__name=breed_name)
        elif user:
            return Cat.objects.filter(owner__username=user)

        return Cat.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @extend_schema(parameters=[
        OpenApiParameter(name='breed',
                         description='Filter cats by breed name',
                         required=False,
                         type=OpenApiTypes.STR,
                         enum=Breed.objects.values_list('name', flat=True)),
        OpenApiParameter(name='owner_name',
                         description='Filter cats by owner name',
                         required=False,
                         type=OpenApiTypes.STR),
    ])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CatsDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CatSerializer

    def get_queryset(self):
        user = self.request.user
        return user.cats_for_owner.all()

class CatsRatingsView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CatRatingsSerializer
    
    def get_queryset(self):
        cat = get_object_or_404(Cat, pk=self.kwargs.get('pk'))
        return CatRating.objects.filter(cat=cat)

    def perform_create(self, serializer):
        cat = get_object_or_404(Cat, pk=self.kwargs.get('pk'))
        user = self.request.user
        if CatRating.objects.filter(rated_by_user=user, cat=cat).exists():
            raise serializers.ValidationError(detail=f'{user.username} already rated {cat.name}')
        else:
            serializer.save(rated_by_user=user, cat=cat)


class BreedListView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class UserRegisterView(CreateAPIView):
    authentication_classes = []
    serializer_class = UserSerializer
