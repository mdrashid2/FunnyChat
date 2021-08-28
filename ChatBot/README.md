# ChatBot
## Funny BOt
This is a coding assignment project wriiten in Python/Django

## Features
- Registration
![Registration Page](screenshot/register.png "Registration Page")

- Login
![Login Page](screenshot/login.png "Login Page")

- User can choose joke any options  ` fat, dumb, stupid `
- After clicking on button user will get funny response through websocket.
![Login Page](screenshot/chat.png "Home Page")

- There is an Options of Audit page, where user can see button clicked audits.
![Login Page](screenshot/audit.png "Audit Page")

## Installation

Requirement ` Python 3.6 , pip & PostgreSql`

` pip install -r requirements.txt `
` create database funny_bot`
configure database in `settings.py` file

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'funny_bot',
        'USER': '<user>',
        'PASSWORD': '<password>',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

` python manage.py migrate `
` python manage.py runserver `
` Create new user & then Login `
