from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from .views import CatsListView, CatsDetailView, BreedListView, UserRegisterView

urlpatterns = [
    # Swagger
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),

    # Auth
    path('auth/token',
         view=TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('auth/token/refresh',
         view=TokenRefreshView.as_view(),
         name='token_refresh'),
    path('auth/register', view=UserRegisterView.as_view()),

    # CATS
    path('cats/', view=CatsListView.as_view()),
    path('cats/<int:pk>/', view=CatsDetailView.as_view()),

    # Breed
    path('breeds/', view=BreedListView.as_view()),
]
