from django.urls import path
from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    path('recipes/', RecipeListView.as_view(), name='list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
]