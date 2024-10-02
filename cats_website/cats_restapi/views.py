from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_spectacular.utils import extend_schema
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.openapi import OpenApiParameter, OpenApiExample

from .models import Breed, Cat
from .serializers import CatSerializer, BreedSerializer, UserSerializer


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
        user = self.request.user
        breed_name = self.request.query_params.get('breed')
        if breed_name:
            return Cat.objects.filter(owner=user, breed__name=breed_name)
        return Cat.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @extend_schema(parameters=[
        OpenApiParameter(name='breed',
                         description='Filter cats by breed name',
                         required=False,
                         type=OpenApiTypes.STR,
                         enum=Breed.objects.values_list('name', flat=True))
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


class BreedListView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class UserRegisterView(CreateAPIView):
    authentication_classes = []
    serializer_class = UserSerializer
