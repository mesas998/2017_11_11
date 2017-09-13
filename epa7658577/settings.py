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
import logging
import datetime
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p$m^awq750!lk#!&y=i09z=q8d^s#+*@wsb=slxjsf=-%6!2qq'

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['www.pp3.cloud']


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
    'django.contrib.flatpages',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'user',
    'nutr',
    'blog',
    'cloudinary',
    'django_countries',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
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

# tacky test for localhost:
if 'Users' in (os.environ['HOME']):
  DEBUG = True
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
  logfile="temporary.log"
else:
  import dj_database_url
  DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}
  DEBUG = False
  logfile="permanent.log"

# Logging
# https://docs.djangoproject.com/en/1.8/topics/logging/

from .log_filters import ManagementFilter

verbose = (
    "[%(asctime)s] %(levelname)s "
    "[%(name)s:%(lineno)s] %(message)s")

"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'remove_migration_sql': {
            '()': ManagementFilter,
        },
    },
    'handlers': {
        'console': {
            'filters': ['remove_migration_sql'],
            'class': 'logging.StreamHandler',
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + "/logfile",
            'maxBytes': 50000,
            'backupCount': 200,
            'formatter': 'verbose',
        },
    },
    'formatters': {
        'verbose': {
            'format': verbose,
            'datefmt': "%Y-%b-%d %H:%M:%S"
        },
    },
    'loggers': {
        'epa7658577': {
            'handlers': ['console'],
            'level': 'INFO',
            'formatter': 'verbose',
            'propogate':True
        },
    },
}
"""
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
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': logfile,
            'when': 'D', # this specifies the interval
            'interval': 1, # defaults to 1, only necessary for other values 
            'backupCount': 10, # how many backup file to keep, 10 days
            'formatter': 'verbose',
        },

    },  
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        '': {
            'handlers': ['file'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        }
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



LANGUAGE_CODE = 'hi-IN'
LANGUAGES = (
    ('af-ZA', _('Afrikaans - South Africa')),
    ('sq-AL', _('Albanian - Albania')),
    ('ar-DZ', _('Arabic - Algeria')),
    ('ar-BH', _('Arabic - Bahrain')),
    ('ar-EG', _('Arabic - Egypt')),
    ('ar-IQ', _('Arabic - Iraq')),
    ('ar-JO', _('Arabic - Jordan')),
    ('ar-KW', _('Arabic - Kuwait')),
    ('ar-LB', _('Arabic - Lebanon')),
    ('ar-LY', _('Arabic - Libya')),
    ('ar-MA', _('Arabic - Morocco')),
    ('ar-OM', _('Arabic - Oman')),
    ('ar-QA', _('Arabic - Qatar')),
    ('ar-SA', _('Arabic - Saudi Arabia')),
    ('ar-SY', _('Arabic - Syria')),
    ('ar-TN', _('Arabic - Tunisia')),
    ('ar-AE', _('Arabic - United Arab Emirates')),
    ('ar-YE', _('Arabic - Yemen')),
    ('hy-AM', _('Armenian - Armenia')),
    ('Cy-az-AZ', _('Azeri (Cyrillic) - Azerbaijan')),
    ('Lt-az-AZ', _('Azeri (Latin) - Azerbaijan')),
    ('eu-ES', _('Basque - Basque')),
    ('be-BY', _('Belarusian - Belarus')),
    ('bg-BG', _('Bulgarian - Bulgaria')),
    ('ca-ES', _('Catalan - Catalan')),
    ('zh-CN', _('Chinese - China')),
    ('zh-HK', _('Chinese - Hong Kong SAR')),
    ('zh-MO', _('Chinese - Macau SAR')),
    ('zh-SG', _('Chinese - Singapore')),
    ('zh-TW', _('Chinese - Taiwan')),
    ('zh-CHS', _('Chinese (Simplified)')),
    ('zh-CHT', _('Chinese (Traditional)')),
    ('hr-HR', _('Croatian - Croatia')),
    ('cs-CZ', _('Czech - Czech Republic')),
    ('da-DK', _('Danish - Denmark')),
    ('div-MV', _('Dhivehi - Maldives')),
    ('nl-BE', _('Dutch - Belgium')),
    ('nl-NL', _('Dutch - The Netherlands')),
    ('en-AU', _('English - Australia')),
    ('en-BZ', _('English - Belize')),
    ('en-CA', _('English - Canada')),
    ('en-CB', _('English - Caribbean')),
    ('en-IE', _('English - Ireland')),
    ('en-JM', _('English - Jamaica')),
    ('en-NZ', _('English - New Zealand')),
    ('en-PH', _('English - Philippines')),
    ('en-ZA', _('English - South Africa')),
    ('en-TT', _('English - Trinidad and Tobago')),
    ('en-GB', _('English - United Kingdom')),
    ('en-US', _('English - United States')),
    ('en-ZW', _('English - Zimbabwe')),
    ('et-EE', _('Estonian - Estonia')),
    ('fo-FO', _('Faroese - Faroe Islands')),
    ('fa-IR', _('Farsi - Iran')),
    ('fi-FI', _('Finnish - Finland')),
    ('fr-BE', _('French - Belgium')),
    ('fr-CA', _('French - Canada')),
    ('fr-FR', _('French - France')),
    ('fr-LU', _('French - Luxembourg')),
    ('fr-MC', _('French - Monaco')),
    ('fr-CH', _('French - Switzerland')),
    ('gl-ES', _('Galician - Galician')),
    ('ka-GE', _('Georgian - Georgia')),
    ('de-AT', _('German - Austria')),
    ('de-DE', _('German - Germany')),
    ('de-LI', _('German - Liechtenstein')),
    ('de-LU', _('German - Luxembourg')),
    ('de-CH', _('German - Switzerland')),
    ('el-GR', _('Greek - Greece')),
    ('gu-IN', _('Gujarati - India')),
    ('he-IL', _('Hebrew - Israel')),
    ('hi-IN', _('Hindi - India')),
    ('hu-HU', _('Hungarian - Hungary')),
    ('is-IS', _('Icelandic - Iceland')),
    ('id-ID', _('Indonesian - Indonesia')),
    ('it-IT', _('Italian - Italy')),
    ('it-CH', _('Italian - Switzerland')),
    ('ja-JP', _('Japanese - Japan')),
    ('kn-IN', _('Kannada - India')),
    ('kk-KZ', _('Kazakh - Kazakhstan')),
    ('kok-IN', _('Konkani - India')),
    ('ko-KR', _('Korean - Korea')),
    ('ky-KZ', _('Kyrgyz - Kazakhstan')),
    ('lv-LV', _('Latvian - Latvia')),
    ('lt-LT', _('Lithuanian - Lithuania')),
    ('mk-MK', _('Macedonian (FYROM)')),
    ('ms-BN', _('Malay - Brunei')),
    ('ms-MY', _('Malay - Malaysia')),
    ('mr-IN', _('Marathi - India')),
    ('mn-MN', _('Mongolian - Mongolia')),
    ('nb-NO', _('Norwegian (Bokmål) - Norway')),
    ('nn-NO', _('Norwegian (Nynorsk) - Norway')),
    ('pl-PL', _('Polish - Poland')),
    ('pt-BR', _('Portuguese - Brazil')),
    ('pt-PT', _('Portuguese - Portugal')),
    ('pa-IN', _('Punjabi - India')),
    ('ro-RO', _('Romanian - Romania')),
    ('ru-RU', _('Russian - Russia')),
    ('sa-IN', _('Sanskrit - India')),
    ('Cy-sr-SP', _('Serbian (Cyrillic) - Serbia')),
    ('Lt-sr-SP', _('Serbian (Latin) - Serbia')),
    ('sk-SK', _('Slovak - Slovakia')),
    ('sl-SI', _('Slovenian - Slovenia')),
    ('es-AR', _('Spanish - Argentina')),
    ('es-BO', _('Spanish - Bolivia')),
    ('es-CL', _('Spanish - Chile')),
    ('es-CO', _('Spanish - Colombia')),
    ('es-CR', _('Spanish - Costa Rica')),
    ('es-DO', _('Spanish - Dominican Republic')),
    ('es-EC', _('Spanish - Ecuador')),
    ('es-SV', _('Spanish - El Salvador')),
    ('es-GT', _('Spanish - Guatemala')),
    ('es-HN', _('Spanish - Honduras')),
    ('es-MX', _('Spanish - Mexico')),
    ('es-NI', _('Spanish - Nicaragua')),
    ('es-PA', _('Spanish - Panama')),
    ('es-PY', _('Spanish - Paraguay')),
    ('es-PE', _('Spanish - Peru')),
    ('es-PR', _('Spanish - Puerto Rico')),
    ('es-ES', _('Spanish - Spain')),
    ('es-UY', _('Spanish - Uruguay')),
    ('es-VE', _('Spanish - Venezuela')),
    ('sw-KE', _('Swahili - Kenya')),
    ('sv-FI', _('Swedish - Finland')),
    ('sv-SE', _('Swedish - Sweden')),
    ('syr-SY', _('Syriac - Syria')),
    ('ta-IN', _('Tamil - India')),
    ('tt-RU', _('Tatar - Russia')),
    ('te-IN', _('Telugu - India')),
    ('th-TH', _('Thai - Thailand')),
    ('tr-TR', _('Turkish - Turkey')),
    ('uk-UA', _('Ukrainian - Ukraine')),
    ('ur-PK', _('Urdu - Pakistan')),
    ('Cy-uz-UZ', _('Uzbek (Cyrillic) - Uzbekistan')),
    ('Lt-uz-UZ', _('Uzbek (Latin) - Uzbekistan')),
    ('vi-VN', _('Vietnamese - Vietnam')),

)
"""
"""
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
print('LOCALE_PATHS: ', LOCALE_PATHS)

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
