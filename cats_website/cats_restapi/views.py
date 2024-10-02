from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from .models import Breed
from .serializers import CatSerializer, BreedSerializer

# Create your views here.


class CatsListView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CatSerializer

    def get_queryset(self):
        user = self.request.user
        return user.cats_for_owner.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    



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