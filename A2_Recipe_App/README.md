# Recipe App

A Django-based web application for discovering, managing, and exploring recipes with intuitive search and filtering capabilities.

## 🎯 Project Overview

The Recipe App is a full-stack Django application that allows users to browse a curated collection of recipes, search by name and cooking time, and view detailed recipe information. The application features a clean, user-friendly interface with beautiful recipe cards, ingredient lists, and cooking instructions.

---

## ✨ Features

- **Recipe Discovery**: Browse a comprehensive collection of recipes with images
- **Advanced Search**: Search recipes by name with partial/wildcard matching
- **Filter by Cooking Time**: Quickly find recipes that fit your schedule
- **Recipe Details**: View full recipe information including ingredients, cooking time, difficulty, and instructions
- **User Authentication**: Login required to access protected recipe views
- **Admin Panel**: Manage recipes, ingredients, and reviews through Django admin
- **Responsive Design**: Mobile-friendly interface that works on all devices
- **Image Support**: Beautiful recipe photos for every dish
- **Reviews System**: Read and write reviews for recipes (v2 feature)

---

## 🛠 Tech Stack

- **Backend**: Django 6.0.1 (Python Web Framework)
- **Frontend**: HTML5, CSS3, Django Templates
- **Database**: SQLite (development), PostgreSQL (production-ready)
- **Server**: Gunicorn 25.1.0 (WSGI HTTP Server)
- **Static Files**: WhiteNoise 6.11.0 (for production serving)
- **Image Processing**: Pillow 12.1.0
- **Data Analysis**: pandas 3.0.0, numpy 2.4.1
- **Visualization**: matplotlib 3.10.8
- **Deployment**: Heroku (cloud hosting)

### Dependencies
```
asgiref==3.11.0
Django==6.0.1
django-cors-headers==4.9.0
djangorestframework==3.16.1
gunicorn==25.1.0
whitenoise==6.11.0
dj-database-url==3.1.0
psycopg2-binary==2.9.11
matplotlib==3.10.8
pandas==3.0.0
numpy==2.4.1
Pillow==12.1.0
```

---

## 📥 Installation Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Recipe-App.git
cd Recipe-App
```

### 2. Create Virtual Environment
**Windows (PowerShell):**
```powershell
python -m venv web-dev
.\web-dev\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
python3 -m venv web-dev
source web-dev/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Navigate to Project Directory
```bash
cd A2_Recipe_App/src
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Load Sample Data (Optional)
```bash
python populate_recipes_with_images.py
```

### 7. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 8. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to access the application.

---

## 🚀 Deployment Instructions

### Deploy to Heroku

#### Prerequisites
- Heroku CLI installed ([heroku.com/downloads](https://devcenter.heroku.com/articles/heroku-cli))
- Git repository initialized
- Heroku account

#### Steps

1. **Create Heroku App**
   ```bash
   heroku create your-app-name
   heroku git:remote -a your-app-name
   ```

2. **Set Environment Variables**
   ```bash
   heroku config:set DJANGO_SECRET_KEY="your-secret-key"
   heroku config:set DEBUG=False
   ```

3. **Deploy Code**
   ```bash
   git push heroku main
   ```

4. **Run Migrations on Production**
   ```bash
   heroku run python A2_Recipe_App/src/manage.py migrate -a your-app-name
   ```

5. **Create Admin User**
   ```bash
   heroku run DJANGO_SUPERUSER_PASSWORD=YourPassword123 python A2_Recipe_App/src/manage.py createsuperuser --noinput --username=admin --email=admin@example.com -a your-app-name
   ```

6. **Populate Sample Data** (Optional)
   ```bash
   heroku run python A2_Recipe_App/src/populate_recipes_with_images.py -a your-app-name
   ```

#### Key Configuration Files
- **Procfile** - Defines how Heroku runs the app
- **requirements.txt** - Python dependencies
- **recipe_project/settings.py** - Django configuration with environment variables
- **.python-version** - Specifies Python version (recommended)

#### Static & Media Files
- Static files are served via WhiteNoise middleware
- Media files (recipe images) are stored in `recipes/static/recipes/images/`
- Both are collected with `python manage.py collectstatic`

---

## 📱 Live URL

**Production**: [https://my-recipe-app-6105574f7d6e.herokuapp.com/](https://my-recipe-app-6105574f7d6e.herokuapp.com/)

**Admin Panel**: [https://my-recipe-app-6105574f7d6e.herokuapp.com/admin/](https://my-recipe-app-6105574f7d6e.herokuapp.com/admin/)

---

## 🔗 GitHub Link

**Repository**: [https://github.com/your-username/Recipe-App](https://github.com/your-username/Recipe-App)

---

## 📂 Project Structure

```
A2_Recipe_App/
├── src/
│   ├── manage.py                          # Django management script
│   ├── db.sqlite3                         # Local database
│   ├── populate_recipes_with_images.py    # Data seeding script
│   ├── recipe_project/
│   │   ├── settings.py                    # Django configuration
│   │   ├── urls.py                        # URL routing
│   │   ├── wsgi.py                        # WSGI configuration
│   │   └── asgi.py                        # ASGI configuration
│   ├── recipes/
│   │   ├── models.py                      # Recipe model definition
│   │   ├── views.py                       # Recipe views
│   │   ├── urls.py                        # Recipe URL patterns
│   │   ├── forms.py                       # Search form
│   │   ├── utils.py                       # Helper functions
│   │   ├── tests.py                       # Test suite
│   │   ├── static/recipes/images/         # Recipe images
│   │   └── templates/recipes/             # Recipe templates
│   ├── ingredients/
│   │   ├── models.py                      # Ingredient model
│   │   └── admin.py                       # Admin configuration
│   ├── reviews/
│   │   ├── models.py                      # Review model
│   │   └── admin.py                       # Admin configuration
│   └── static/                            # Global static files
├── Procfile                               # Heroku deployment config
├── requirements.txt                       # Python dependencies
├── .python-version                        # Python version specification
└── README.md                              # This file
```

---

## 👤 Admin Credentials

**Production Admin**
- **Username**: `mentorCF`
- **Password**: `Ment0r@CareerF0undry`

---

## 🧪 Testing

Run the test suite:
```bash
cd A2_Recipe_App/src
python manage.py test recipes
```

All tests are passing ✅

---

## 📝 Notes

- The app uses Django's built-in authentication for user management
- Recipe images are served via WhiteNoise in production
- The database is configured to use SQLite locally and supports PostgreSQL via `DATABASE_URL` on Heroku
- CSRF protection is enabled on all forms
- The SECRET_KEY is loaded from environment variables in production

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is part of the Career Foundry Python for Web Developers specialization.

---

**Last Updated**: February 13, 2026
