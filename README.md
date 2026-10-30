### Productly 🛒

A basic web application built with Django to manage products. This was my Foundation Year project in 2024, one of my first experiences building a website with a backend framework.

### 📖 About the project

When I built this project I was just starting to code and wanted to understand how a website works "under the hood": how URLs, views, HTML templates, and the database connect to each other.
Productly is a simple web page where users can [add / view / edit / delete] products using forms and a database.


### ✨ What does it do?
Displays a home page with product information.
Lets users add products through a form.
Uses reusable HTML templates (base.html) to keep the same layout across all pages.
Includes Django's built-in admin panel to manage data.

### 🛠️ Tech stack
Python 3
Django
HTML (Django templates)
Pipenv for the virtual environment and dependencies


### 📁 Project structure

```
Workspace/
├── productly/          # Main project configuration
│   ├── settings.py     # Django settings
│   ├── urls.py         # Main URLs
│   ├── views.py
│   ├── asgi.py
│   └── wsgi.py
├── productos/          # Main app
│   ├── models.py       # Models (database structure)
│   ├── views.py        # Page logic
│   ├── forms.py        # Forms
│   ├── urls.py         # App URLs
│   ├── admin.py        # Admin panel configuration
│   ├── migrations/     # Database change history
│   ├── templates/
│   └── templatetags/   # Custom template tags
├── templates/          # Global templates
│   ├── base.html       # Base template
│   ├── form_snippet.html
│   └── inicio.html     # Home page
├── manage.py
├── Pipfile
├── requirements.txt
└── db.sqlite3

```

### 🌱 What I learned
- How a Django project is organized (project vs. apps).
- The MVT pattern (Model – View – Template).
- Creating models and handling migrations.
- Setting up URLs and views.
- Using Django forms to save data.
- Reusing HTML with template inheritance ({% extends %} and {% block %}).
- Working with virtual environments and dependency files.
- Using Git to save and organize my work.

### 🔮 Future improvements
- Improve the design with CSS / Bootstrap.
- Add user authentication.
- Add product search and filters.
- Add product images.
- Write automated tests.
- Deploy the app online.


👤 Author

[Heric Perez] Student at [Regent College London] 
🔗 [[GitHub](https://github.com/Heric127/productly)]
