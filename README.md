# DevSearch

Sourcode and Resources for **devsearch**

## Installation

* 1 - clone repo <https://github.com/minhtran241/devsearch>
* 2 - create a virtual environment and activate
  * - pip install virtualenv
  * - virtualenv envname
  * - envname\scripts\activate
* 3 - cd into project "cd devsearch"
* 4 - pip install -r requirements.txt
* 5 - python manage.py runserver

## Features

* Share Projects
* Message other developers
* Rate others work
* Search other developers

## Tech Stack

* Django
* Postgres
* Django REST Framework

<!-- # Home Page
<img src="./resources/images/Devsearch Home.jpg">  

# Projects Page
<img src="./resources/images/DevSearch Projects.jpg">  

# Profile Page
<img src="./resources/images/Devsearch Profile.jpg">  

# User Inbox
<img src="./resources/images/Devsearch Inbox.jpg">   -->

## Set up & Migrate Database

1. Go to the `setting.py` and change this lines up to your PostgreSQL account

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'devSearch',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': ENV['DB_PASS']
    }
}
```

2. Run the migrations

```sh
python manage.py migrate
```

## Set up Email backend

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ENV['EMAIL']
EMAIL_HOST_PASSWORD = ENV['EMAIL_PASS']
```
