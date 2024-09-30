from rest_framework.serializers import ModelSerializer

from .models import Cat


class CatSerializer(ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'