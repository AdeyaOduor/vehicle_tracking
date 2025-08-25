
mkdir vehicle_tracking
cd vehicle_tracking
django-admin startproject config .
mkdir apps templates static media tests

cd apps
python3 ../manage.py startapp core
python3 ../manage.py startapp users
python3 ../manage.py startapp vehicles
python3 ../manage.py startapp dashboard

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
    └── conftest.py


python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
