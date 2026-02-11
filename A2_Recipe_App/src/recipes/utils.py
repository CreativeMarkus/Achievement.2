from io import BytesIO
import base64
import matplotlib.pyplot as plt
import pandas as pd
from .models import Recipe


def get_graph():
    """
    Converts matplotlib plot to base64 encoded PNG image for embedding in HTML.
    This function handles the low-level image processing details.
    """
    # Create a BytesIO buffer for the image
    buffer = BytesIO()
    
    # Create a plot with a BytesIO object as a file-like object. Set format to png
    plt.savefig(buffer, format='png')
    
    # Set cursor to the beginning of the stream
    buffer.seek(0)
    
    # Retrieve the content of the file
    image_png = buffer.getvalue()
    
    # Encode the bytes-like object
    graph = base64.b64encode(image_png)
    
    # Decode to get the string as output
    graph = graph.decode('utf-8')
    
    # Free up the memory of buffer
    buffer.close()
    
    # Return the image/graph
    return graph


def get_chart(chart_type, data, **kwargs):
    """
    Generates different types of charts based on user input.
    
    Args:
        chart_type: User input for type of chart ('#1' for bar, '#2' for pie, '#3' for line)
        data: Pandas DataFrame containing recipe data
        **kwargs: Additional parameters like labels
    
    Returns:
        Base64 encoded PNG image string of the chart
    """
    # Switch plot backend to AGG (Anti-Grain Geometry) - to write to file
    # AGG is preferred solution to write PNG files
    plt.switch_backend('AGG')
    
    # Specify figure size
    fig = plt.figure(figsize=(8, 4))
    
    # Select chart_type based on user input from the form
    if chart_type == '#1':
        # Bar chart: cooking time categories vs recipe count
        # Create cooking time categories
        cooking_time_categories = pd.cut(
            data['cooking_time'],
            bins=[0, 15, 30, float('inf')],
            labels=['Quick (<15 min)', 'Medium (15-30 min)', 'Long (>30 min)']
        )
        category_counts = cooking_time_categories.value_counts().sort_index()
        
        plt.bar(range(len(category_counts)), category_counts.values)
        plt.xticks(range(len(category_counts)), category_counts.index, rotation=45, ha='right')
        plt.ylabel('Number of Recipes')
        plt.xlabel('Cooking Time Category')
        plt.title('Recipe Count by Cooking Time Category')
    
    elif chart_type == '#2':
        # Pie chart: distribution of recipes by cooking time
        cooking_time_categories = pd.cut(
            data['cooking_time'],
            bins=[0, 15, 30, float('inf')],
            labels=['Quick (<15 min)', 'Medium (15-30 min)', 'Long (>30 min)']
        )
        category_counts = cooking_time_categories.value_counts()
        
        plt.pie(
            category_counts.values,
            labels=category_counts.index,
            autopct='%1.1f%%',
            startangle=90
        )
        plt.title('Recipe Distribution by Cooking Time')
    
    elif chart_type == '#3':
        # Line chart: cumulative recipe count (by ID, representing order)
        data_sorted = data.sort_values('id')
        cumulative_count = range(1, len(data_sorted) + 1)
        
        plt.plot(data_sorted['id'].values, cumulative_count, marker='o')
        plt.ylabel('Cumulative Recipe Count')
        plt.xlabel('Recipe ID')
        plt.title('Cumulative Recipe Count Over Time')
        plt.grid(True, alpha=0.3)
    
    else:
        print('unknown chart type')
    
    # Specify layout details
    plt.tight_layout()
    
    # Render the graph to file
    chart = get_graph()
    
    # Clear the current figure
    plt.clf()
    
    return chart


def prepare_recipe_data(recipes_queryset):
    """
    Converts a Recipe QuerySet to a pandas DataFrame for data analysis.
    
    Args:
        recipes_queryset: Django QuerySet of Recipe objects
    
    Returns:
        Pandas DataFrame with recipe data
    """
    if not recipes_queryset.exists():
        return None
    
    # Convert queryset to list of dictionaries
    data = list(recipes_queryset.values('id', 'name', 'cooking_time'))
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    return df
