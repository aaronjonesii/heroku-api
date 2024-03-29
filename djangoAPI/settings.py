"""
Django settings for djangoAPI project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'eibf&bje^skjv4$osd-z9+3vnm(jb0u@&w68t#5_e8s9-lbfhv-')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
# DEBUG = True
DEBUG = os.environ.get('DEBUG', False)

ALLOWED_HOSTS = [
    'api-anonsys-tech.herokuapp.com',
    'api.anonsys.tech',
    'localhost',
    # '93.188.164.182',
    # 'anonsys.tech'
]

CORS_ORIGIN_WHITELIST = (
    'localhost:9999',
    'anonsys.tech',
    # '93.188.164.182',
)
# CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangoAPI.api',
    'rest_framework',
    'corsheaders',
    'rest_framework_tracking',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'djangoAPI.urls'

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

WSGI_APPLICATION = 'djangoAPI.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    # 'default': {
    #     'NAME': 'anonsys_db',
    #     'ENGINE': 'mysql.connector.django',
    #     'USER': 'root',
    #     # 'PASSWORD': '',
    #     'PASSWORD': os.environ['DJANGO_DATABASE_PWD'],
    #     'OPTIONS': {
    #         'autocommit': False,
    #     },
    # }
}
import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



# FOR DJANGO REST FRAMEWORK PAGINATION
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # ),
    # 'DEFAULT_PARSER_CLASSES': (
    #     'rest_framework.parsers.JSONParser',
    # )
}


# Sentry Monitoring
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
sentry_sdk.init(
    dsn="https://fef4d776407348b3b5d6df23706e2e32@sentry.io/1371566",
    integrations=[DjangoIntegration()]
)


EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
