from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
import pandas as pd
from .models import Recipe
from .forms import RecipeSearchForm
from .utils import prepare_recipe_data, get_chart

def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'


def recipe_search(request):
    """
    Function-based view for searching recipes and displaying visualizations.
    Implements search by recipe name and cooking time, with multiple chart options.
    """
    form = RecipeSearchForm(request.POST or None)
    recipes_df = None
    chart = None
    search_results = None
    chart_type = None
    
    # Check if form was submitted via POST
    if request.method == 'POST' and form.is_valid():
        # Get search criteria from form
        recipe_name = form.cleaned_data.get('recipe_name', '').strip()
        cooking_time = form.cleaned_data.get('cooking_time')
        chart_type = form.cleaned_data.get('chart_type')
        
        # Build QuerySet based on search criteria
        queryset = Recipe.objects.all()
        
        # Filter by recipe name (case-insensitive, partial match)
        if recipe_name:
            queryset = queryset.filter(name__icontains=recipe_name)
        
        # Filter by cooking time
        if cooking_time:
            queryset = queryset.filter(cooking_time__lte=cooking_time)
        
        # Store search results
        search_results = queryset
        
        # Convert to DataFrame for analysis and charting
        if queryset.exists():
            recipes_df = prepare_recipe_data(queryset)
            
            # Generate chart if chart type is selected
            if chart_type and recipes_df is not None:
                try:
                    chart = get_chart(chart_type, recipes_df)
                except Exception as e:
                    print(f"Error generating chart: {e}")
                    chart = None
    
    # Show all recipes if no search criteria provided
    elif request.method == 'GET' and 'show_all' in request.GET:
        queryset = Recipe.objects.all()
        search_results = queryset
        
        # Prepare data and generate default chart
        if queryset.exists():
            recipes_df = prepare_recipe_data(queryset)
            chart = get_chart('#1', recipes_df)  # Default to bar chart
    
    # Prepare context dictionary
    context = {
        'form': form,
        'search_results': search_results,
        'chart': chart,
        'recipes_df': recipes_df,
    }
    
    return render(request, 'recipes/recipe_search.html', context)
