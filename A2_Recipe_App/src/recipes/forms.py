from django import forms

CHART_CHOICES = (
    ('#1', 'Bar Chart'),
    ('#2', 'Pie Chart'),
    ('#3', 'Line Chart')
)

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
