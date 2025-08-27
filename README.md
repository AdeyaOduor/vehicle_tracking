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


cd /path/to/your/vehicle_tracking
git remote add origin https://github.com/AdeyaOduor/vehicle_tracking.git  # if not added
git fetch origin
git rebase origin/main
# resolve conflicts if any
git rebase --continue  # after resolving
git push origin <your_branch_name> --force  # if needed# vehicle_tracking
