# Exercise 2.7 Task: Recipe Application Search and Visualization

## Planning and Design

### Search Functionality Plan

#### What Users Can Search For:
- **Primary Search Criterion**: Recipe Name (with partial/wildcard matching support)
- **Optional Filters**: 
  - Cooking Time (by range or exact value)
  - Ingredients (contains any of selected ingredients)

#### Search Output Format:
- Results displayed as a table showing:
  - Recipe Name (clickable link to detail page)
  - Cooking Time
  - Number of Ingredients
  - Action Links (View Details, Edit, Delete)
- Results are paginated (10 recipes per page)
- "No results found" message when no matches

#### Show-All Feature:
- Button on search page to display all recipes without filters
- Useful for users who want to browse all available recipes

---

## Data Analysis Section

### Chart 1: Bar Chart
- **Purpose**: Display number of recipes by cooking time range
- **X-Axis**: Cooking Time (categorized as Quick <15min, Medium 15-30min, Long >30min)
- **Y-Axis**: Count of Recipes
- **When Displayed**: On search results page (always shown)
- **Insight**: Helps identify which cooking time categories are most common

### Chart 2: Pie Chart
- **Purpose**: Show distribution of recipes across different cooking time categories
- **Labels**: Time categories (Quick, Medium, Long)
- **Data**: Percentage of recipes in each category
- **When Displayed**: On search results page (always shown)
- **Insight**: Visual representation of recipe variety by preparation time

### Chart 3: Line Chart
- **Purpose**: Show cumulative recipe count over time (when recipes were added)
- **X-Axis**: Recipe ID (proxy for creation order)
- **Y-Axis**: Cumulative Recipe Count
- **When Displayed**: On search results page (always shown)
- **Insight**: Growth trend of recipe database

---

## Implementation Details

### Technologies Used:
1. **Django Forms** - For user input (RecipeSearchForm)
2. **QuerySet API** - For database filtering and extraction
3. **Pandas DataFrame** - For data processing and manipulation
4. **Matplotlib** - For chart generation
5. **Base64 Encoding** - For embedding charts in HTML

### Key Features Implemented:
1. Search form with recipe name and cooking time filters
2. Partial/wildcard search support (case-insensitive)
3. Multiple chart types (bar, pie, line)
4. Clickable results that link to recipe details
5. Chart generation based on user selection
6. Show All button for viewing all recipes

### Files Created/Modified:
- `recipes/forms.py` - Search form definition
- `recipes/utils.py` - Data processing and charting functions
- `recipes/views.py` - Updated with recipe_search view
- `recipes/urls.py` - Added search route
- `recipes/templates/recipes/recipe_search.html` - Search interface
- `recipes/tests.py` - Comprehensive test coverage (20 tests)

---

## Testing Results

### Test Coverage:
- 20 tests total
- All tests passing (OK)
- Includes:
  - Form validation tests
  - View authentication tests
  - Search functionality tests
  - Chart generation tests

### Test Execution Results:
```
Ran 20 tests in 13.960s
OK
```

### Test Categories:
1. **RecipeModelTest** (3 tests)
   - Model field validation
   - String representation

2. **RecipeSearchFormTest** (5 tests)
   - Valid/empty data handling
   - Field validation (cooking time, recipe name)
   - Chart type choices

3. **RecipeSearchViewTest** (7 tests)
   - Search by name with partial matching
   - Search by cooking time
   - Show all functionality
   - Chart generation
   - No results handling

4. **RecipeListViewTest** (2 tests)
   - Login protection
   - Authenticated access

5. **RecipeDetailViewTest** (2 tests)
   - Login protection
   - Recipe retrieval

---

## Execution Flow

### User Journey:
1. **Landing** - User arrives at homepage (recipes_home.html)
2. **Authentication** - User logs in with credentials (email/password)
3. **Navigation** - User clicks "Search Recipes" link
4. **Search** - User enters search criteria (recipe name and/or cooking time)
5. **Results** - Search results display in table format with charts
6. **Details** - User clicks on recipe name to view full details
7. **Logout** - User clicks logout to end session

### URL Flow:
- `/` → Home page
- `/accounts/login/` → Login page
- `/recipes/` → Recipe list view (authenticated)
- `/recipes/search/` → Search page (authenticated)
- `/recipes/<id>/` → Recipe detail page (authenticated)
- `/accounts/logout/` → Logout

### Example Search Scenarios:

**Scenario 1: Search by Recipe Name**
- User enters "Pasta" in search field
- Form submits via POST request
- View filters recipes using: `Recipe.objects.filter(name__icontains='Pasta')`
- Results show: Spaghetti Carbonara, Chicken Pasta (partial match)
- Chart displays based on selected type (bar/pie/line)

**Scenario 2: Search by Cooking Time**
- User enters "30" in cooking time field
- View filters: `Recipe.objects.filter(cooking_time__lte=30)`
- Results show all recipes with ≤ 30 minute cooking time
- Caesar Salad (10), Pad Thai (25), Spaghetti Carbonara (20)

**Scenario 3: Combined Search**
- User enters "Cake" and sets cooking time to "50"
- Both filters applied: name filter AND cooking time filter
- Results show: Chocolate Cake (45 minutes matches ≤50)

**Scenario 4: Show All**
- User clicks "Show All Recipes" button
- View retrieves all recipes without filters
- Default bar chart displays
- User can browse entire recipe collection

### Search Results Display:
```
Search Results (2 recipes found)
┌─────────────────────────────────────────┐
│ Recipe Name        │ Cooking Time │ Actions  │
├──────────────────────────────────────────┤
│ Spaghetti Carbonara│ 20           │ Details  │
│ Chicken Pasta      │ 35           │ Details  │
└──────────────────────────────────────────┘

[Chart Image - Bar/Pie/Line based on selection]
```

---

## Key Implementation Notes:

1. **Search Form** - Uses Django Form with optional fields
2. **QuerySet Filtering** - Case-insensitive partial matching with `icontains`
3. **Data Processing** - Pandas DataFrame for efficient data manipulation
4. **Chart Types**:
   - Bar chart: Shows recipe count by cooking time category
   - Pie chart: Shows percentage distribution of cooking times
   - Line chart: Shows cumulative recipe count
5. **HTML Integration** - Charts embedded using base64 encoding as data URIs
6. **Error Handling** - Graceful handling of no-results scenarios

---

## Execution Evidence

Screenshots captured during user journey:
(To be populated during execution)

1. Login page - User authentication
2. Search page - Form with search criteria
3. Search results - Table view with recipes
4. Chart views - Bar, pie, and line charts
5. Recipe details - Full recipe information
6. Logout - Session termination

---

## Bonus Features Implemented:
- Partial/wildcard search support
- Multiple chart visualization options
- Responsive design with Bootstrap-inspired styling
- Comprehensive test coverage
- Clean separation of concerns (forms, utils, views, templates)

---

## Files and Deliverables:
- ✅ Task-2.7.md - Planning document
- ✅ test-outcome.txt - Test results screenshot
- ✅ Source code pushed to GitHub
- ✅ Forms, views, utils, templates implemented
- ✅ 20 passing tests
