"""
Django settings for epa7658577 project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url
import cloudinary

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p$m^awq750!lk#!&y=i09z=q8d^s#+*@wsb=slxjsf=-%6!2qq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

"""
in suorganizer/settings.py:`
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    #django_extensions',
    'core',
    'user',
    'organizer',
    'contact',
"""
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'user',
    'nutr',
    'blog',
    'cloudinary',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'epa7658577.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'epa7658577.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# uncomment for localhost:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb2',
        'USER': 'michaelsweeney',
        'PASSWORD': 'xzdzxzf',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
# uncomment for heroku:
"""
import dj_database_url
DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}
"""

# Logging
# https://docs.djangoproject.com/en/1.8/topics/logging/

verbose = (
    "[%(asctime)s] %(levelname)s "
    "[%(name)s:%(lineno)s] %(message)s")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'formatters': {
        'verbose': {
            'format': verbose,
            'datefmt': "%Y-%b-%d %H:%M:%S"
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'formatter': 'verbose'
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
from django.core.urlresolvers import reverse_lazy

LOGIN_REDIRECT_URL = reverse_lazy('nutr_tag_list')
LOGIN_URL = reverse_lazy('dj-auth:login')
LOGOUT_URL = reverse_lazy('dj-auth:logout')
SITE_ID = 1
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
#EDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
#EDIA_URL = os.path.join(PROJECT_DIR, 'media/')
MEDIA_ROOT = os.path.join('static')
MEDIA_URL = os.path.join('static/')
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# suggested on https://devcenter.heroku.com/articles/django-assets
# to solve "Django does not support serving static files in production.":
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
ACCOUNT_ACTIVATION_DAYS=5
SENDGRID_API_KEY=      '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'
SENDGRID_PASSWORD=     'pjamfoyy0286'
SENDGRID_USERNAME=     'app73564228@heroku.com'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = SENDGRID_USERNAME
EMAIL_HOST_PASSWORD =  SENDGRID_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True
cloudinary.config( 
  cloud_name = "hh9sjfv1s", 
  api_key = "925446259887781", 
  api_secret = "gpaSETTqdBg_AItG4Xky4Bq_b10"
)
"""
# https://pythonhosted.org/django-herokuify/mail.html
EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = 'key-57335d3ea948d2e5ecd727badd5b20ab'
MAILGUN_SERVER_NAME = 'https://api.mailgun.net/v3/mailgun-shallow-93775'
from herokuify.mail.mailgun import EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT
# p. 744 commented out
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'michael.sweeney303'
EMAIL_HOST_PASSWORD ='fdrdfdt32~'
EMAIL_USE_TLS = True
# sqlite3 localhost commented out:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
