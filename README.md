# Django CRM Learning Project

A Django-based Customer Relationship Management (CRM) learning project. The application includes an accounts app with customer, product, and order-related functionality, Django templates, and a SQLite development database configuration.

## Application structure

```text
crm/
├── accounts/
│   ├── migrations/
│   ├── templates/accounts/
│   ├── admin.py
│   ├── filters.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── crm/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

## Technology

Python · Django 5 · Django ORM · SQLite · HTML/CSS

## Local setup

1. Create and activate a virtual environment.
2. Install Django and django-filter.
3. Set the required environment variables in your terminal.
4. From the `crm/` directory, run migrations and start the development server.

Example environment configuration:

```powershell
$env:DJANGO_SECRET_KEY = "generate-a-new-local-secret"
$env:DJANGO_DEBUG = "true"
$env:DJANGO_ALLOWED_HOSTS = "127.0.0.1,localhost"
python manage.py migrate
python manage.py runserver
```

Do not use the example secret in production. Generate a strong secret for each environment and store it outside source control.

## Security and deployment notes

- The Django settings now require `DJANGO_SECRET_KEY` from the environment; the previously committed development key is no longer used by the current version.
- `DEBUG` is off by default and should remain off in production.
- Configure `ALLOWED_HOSTS` for the actual deployment hostnames.
- The repository includes a SQLite database file. Review it to ensure it contains only synthetic/demo records before keeping it public; do not publish customer or personal information.
- A local Python environment was previously committed. It has been removed from the current branch; install dependencies in a local virtual environment instead.

This repository is best presented as a Django learning/full-stack supporting project, not as a core data engineering flagship.
