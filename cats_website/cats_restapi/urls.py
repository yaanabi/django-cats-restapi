from django.urls import path
from .views import CatsListView, CatsDetailView

urlpatterns = [
    path('cats/', view=CatsListView.as_view()),
    path('cats/<int:pk>/', view=CatsDetailView.as_view()),
    
]
