from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer
from drf_spectacular.openapi import OpenApiExample

from django.contrib.auth.models import User

from .models import Cat, Breed, CatRating


@extend_schema_serializer(examples=[
    OpenApiExample(
        'Valid example 1',
        summary='Example request',
        description='''
                name: str; Cat name; max length 255 chars,
                breed: str; Breed name from breed db table,
                age: int; Age in full months,
                color: str; Cat color; max length 100 chars,
                description: str; Cat description; max length 500 chars.
                ''',
        value={
            'name': 'Vasya',
            'breed': 'Persian',
            'age': 1,
            'color': 'white',
            'description': 'Persian kitty!'
        },
        request_only=True,
    ),
])
class CatSerializer(serializers.ModelSerializer):
    breed = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Breed.objects.all(),
        error_messages={
            'does_not_exist':
            'Breed with name does not exist. Please choose a valid breed.',
            'invalid': 'Invalid breed selection.'
        })
    owner = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Cat
        fields = ('id', 'name', 'breed', 'age', 'color', 'description',
                  'owner')


class CatRatingsSerializer(serializers.ModelSerializer):
    cat = serializers.SlugRelatedField(slug_field='name', read_only=True)
    rated_by_user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = CatRating
        fields = ('id', 'rating', 'cat', 'rated_by_user')


class BreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breed
        fields = (
            'id',
            'name',
        )


@extend_schema_serializer(examples=[
    OpenApiExample(
        'Valid example 1',
        summary='Example request',
        value={
            'username': 'Vasya',
            'password': 'qwerty',
        },
        request_only=True,
    ),
])
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
        )

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], )
        user.set_password(validated_data['password'])
        user.save()
        return user
