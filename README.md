<<<<<<< HEAD

mkdir vehicle_tracking
cd vehicle_tracking
django-admin startproject config .
mkdir apps templates static media tests

cd apps
python3 ../manage.py startapp core
python3 ../manage.py startapp users
python3 ../manage.py startapp vehicles
python3 ../manage.py startapp dashboard

=======
>>>>>>> 3cbe1ba (modified a file)
vehicle_tracking/
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── .gitignore
├── README.md
├── config/
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── admin.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── managers.py
│   │   └── utils.py
│   ├── users/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── admin.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── backends.py
│   ├── vehicles/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── admin.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── api.py
│   └── dashboard/
│       ├── __init__.py
│       ├── models.py
│       ├── admin.py
│       ├── views.py
│       ├── urls.py
│       └── utils.py
├── templates/
│   ├── base.html
│   ├── includes/
│   │   ├── header.html
│   │   ├── footer.html
│   │   ├── navigation.html
│   │   └── messages.html
│   ├── registration/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── password_reset.html
│   ├── core/
│   │   ├── index.html
│   │   └── landing.html
│   ├── vehicles/
│   │   ├── vehicle_list.html
│   │   ├── vehicle_detail.html
│   │   ├── vehicle_form.html
│   │   └── assign_driver.html
│   ├── dashboard/
│       ├── national.html
│       ├── county.html
│       ├── subcounty.html
│       └── components/
│           ├── stats_cards.html
│           ├── vehicle_map.html
│           └── charts.html
├── static/
│   ├── css/
│   │   ├── style.css
│   │   └── material-ui.css
│   ├── js/
│   │   ├── main.js
│   │   ├── charts.js
│   │   └── map.js
│   ├── images/
│   │   ├── logo.png
│   │   └── favicon.ico
│   └── vendors/
│       ├── material-ui/
│       ├── leaflet/
│       └── chartjs/
├── media/
│   ├── vehicles/
│   └── profiles/
└── tests/
    ├── __init__.py
    ├── test_models.py
    ├── test_views.py
    ├── test_forms.py
<<<<<<< HEAD
    └── conftest.py


<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}FleetTrack - Vehicle Management System{% endblock %}</title>
    <!-- Material Icons -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <!-- CSS -->
    <link rel="stylesheet" href="{% static 'css/material-ui.css' %}">
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    {% block extra_css %}{% endblock %}
</head>
<body>
    {% include 'includes/header.html' %}
    
    {% include 'includes/navigation.html' %}
    
    <main class="main-content">
        {% include 'includes/messages.html' %}
        
        {% block content %}
        {% endblock %}
    </main>
    
    {% include 'includes/footer.html' %}
    
    <!-- JavaScript -->
    <script src="{% static 'js/main.js' %}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>

# Deployment Steps
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

# Docker file
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]

# docker-compose.yml:
version: '3.8'

services:
  web:
    build: .
    command: gunicorn config.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - static_volume:/app/static
      - media_volume:/app/media
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db
      - redis

  db:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    env_file:
      - .env

  redis:
    image: redis:7-alpine

  celery:
    build: .
    command: celery -A config.celery_app worker --loglevel=info
    volumes:
      - .:/app
    env_file:
      - .env
    depends_on:
      - redis
      - db

volumes:
  postgres_data:
  static_volume:
  media_volume:


# gitignore
# Django
*.log
*.pot
*.pyc
__pycache__/
local_settings.py
db.sqlite3
media
.env
.env.prod

# Virtual environment
venv/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
=======
    └── conftest.py
>>>>>>> 3cbe1ba (modified a file)
