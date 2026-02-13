from django.urls import path
from .views import (
    home, about, RecipeListView, RecipeDetailView, recipe_search,
    RecipeCreateView, RecipeUpdateView, RecipeDeleteView
)

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('recipes/', RecipeListView.as_view(), name='list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/edit/', RecipeUpdateView.as_view(), name='recipe-edit'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('search/', recipe_search, name='recipe-search'),
]