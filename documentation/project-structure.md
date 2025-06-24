# Project Structure

The LawAI backend is organized into multiple Django apps, each handling specific functionality of the legal practice management system.

## Directory Structure

```
├── core/                   # Project core configuration
│   ├── settings.py        # Project settings
│   ├── urls.py           # Main URL configuration
│   ├── asgi.py           # ASGI configuration
│   └── wsgi.py           # WSGI configuration
├── lawyer/                # Lawyer management app
│   ├── models.py         # Lawyer data models
│   ├── views.py          # API views
│   ├── urls.py           # URL routing
│   └── serializers.py    # Data serializers
├── client/               # Client management app
│   ├── models.py         # Client data models
│   ├── views.py          # API views
│   ├── urls.py           # URL routing
│   └── serializers.py    # Data serializers
├── cases/                # Case management app
│   ├── models.py         # Case data models
│   ├── views.py          # API views
│   ├── urls.py           # URL routing
│   └── serializers.py    # Data serializers
├── document/             # Document management app
│   ├── models.py         # Document data models
│   ├── views.py          # API views
│   ├── urls.py          # URL routing
│   └── serializers.py    # Data serializers
├── tasks/                # Task management app
│   ├── models.py         # Task data models
│   ├── views.py         # API views
│   ├── urls.py          # URL routing
│   └── serializers.py    # Data serializers
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

## Apps Description

### Core
The core application contains the project's main configuration, including settings, main URL routing, and deployment configurations.

### Lawyer App
Manages lawyer profiles, authentication, and related functionalities.

### Client App
Handles client information, relationships with lawyers, and client-specific data.

### Cases App
Manages legal cases, including case details, status, and relationships with lawyers and clients.

### Document App
Handles document management, including storage, categorization, and version control.

### Tasks App
Manages tasks, deadlines, and assignments for lawyers and cases.
