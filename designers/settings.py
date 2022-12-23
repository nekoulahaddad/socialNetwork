"""
Django settings for designers project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
# import django_heroku
import dj_database_url
from  decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-uqd%2e79c7c_ifaiqviqcz3q7=pf9sj98!cw21_7a+$315__2c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['92.63.103.180', 'designerspython.herokuapp.com','https://designerspython.herokuapp.com','http://designerspython.herokuapp.com', '127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'notifications',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'django_extensions',
    'blog',
    'members',
    'django.contrib.humanize',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'designers.urls'

DJANGO_NOTIFICATIONS_CONFIG = { 'USE_JSONFIELD': True}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'designers.wsgi.application'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'youaremyfuturewife@gmail.com'
EMAIL_HOST_PASSWORD = 'bravo222'
ADMINS = [('nekoula', 'nekoulahaddad@gmail.com'), ('haddad', 'nekoulahaddad2@gmail.com')]

WHITENOISE_USE_FINDERS = True



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'mysite.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'MYAPP': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}







DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]




LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'
MEDIA_URL = '/media/' #for development

# MEDIA_URL = '/static/mediafiles/' #for production

LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




#the directory that used to upload images by user
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# MEDIA_ROOT = os.path.join(BASE_DIR,'staticfiles','mediafiles')
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

#if i have additional static files rather than the files, which is located in the static folder in each app, i can put this additional files in this folder and then collect it to the desired directory, which used in production(in our case 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
    )

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# django_heroku.settings(locals())