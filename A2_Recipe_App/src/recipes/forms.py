from django import forms
from .models import Recipe

CHART_CHOICES = (
    ('#1', 'Bar Chart'),
    ('#2', 'Pie Chart'),
    ('#3', 'Line Chart')
)

class RecipeForm(forms.ModelForm):
    """Form for creating and editing recipes"""
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'instructions', 'cooking_time', 'pic']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Recipe Name'
            }),
            'ingredients': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ingredients (one per line)',
                'rows': 5
            }),
            'instructions': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter cooking instructions',
                'rows': 5
            }),
            'cooking_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cooking time in minutes'
            }),
            'pic': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }

class RecipeSearchForm(forms.Form):
    """Form for searching recipes with optional chart visualization"""
    recipe_name = forms.CharField(
        max_length=120,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter recipe name (e.g., "pizza", "cake")',
            'class': 'form-control'
        }),
        label='Recipe Name'
    )
    
    cooking_time = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Max cooking time in minutes',
            'class': 'form-control'
        }),
        label='Max Cooking Time (minutes)',
        min_value=0
    )
    
    chart_type = forms.ChoiceField(
        choices=CHART_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label='Chart Type',
        initial='#1'
    )
