import os
from csg.environment.client import EnvironmentClient
from corsheaders.defaults import default_headers
from csg.libs.django.settings.databases.csgapi import DATABASE_DEV, DATABASE_PRODUCTION, DATABASE_STAGING, DATABASE_QA

environment_client = EnvironmentClient()

ROOT_URLCONF = 'abacusinventory.urls'
WSGI_APPLICATION = 'abacusinventory.wsgi.application'
ASGI_APPLICATION = 'abacusinventory.asgi.application'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '%^aiul=h!@_qf-quubrcu%v+2kwad$u4@f71q+spw#$5rh^lbi'
DEBUG = False
LOGGING_CONFIG = None  # Logging to allow for default use of CSG logger
LOCKDOWN_ADMIN = False

ALLOWED_HOSTS = [
    '*'
]

INSTALLED_APPS = [
    'rest_framework',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'api',
    'corsheaders',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'api.middleware.csrf_exempt.CsrfExemptSessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATIC_URL_DEV = '/static/'
STATIC_URL_QA = 'https://storage.googleapis.com/abacusinventory-qa-static/'
STATIC_URL_STAGING = 'https://storage.googleapis.com/abacusinventory-staging-static/'
STATIC_URL_PROD = 'https://storage.googleapis.com/abacusinventory-static/'

################################################################################
# ENVIRONMENT SPECIFIC SETTINGS
################################################################################
if EnvironmentClient.is_qa():
    DEBUG = True
    STATIC_URL = STATIC_URL_QA
    DATABASES = {'default': DATABASE_QA}
    CORS_ORIGIN_WHITELIST = [
        "https://abacusinventory-qa.appspot.com",
        "https://api-qa.abacus.dental"
    ]
    CORS_ALLOW_HEADERS = list(default_headers) + [
        'x-api-key',
    ]
elif EnvironmentClient.is_staging():
    DEBUG = False
    STATIC_URL = STATIC_URL_STAGING
    DATABASES = {'default': DATABASE_STAGING}
    CORS_ORIGIN_WHITELIST = [
        "https://abacusinventory-staging.appspot.com",
        "https://api-staging.abacus.dental"
    ]
    CORS_ALLOW_HEADERS = list(default_headers) + [
        'x-api-key',
    ]
elif EnvironmentClient.is_production():
    DEBUG = False
    STATIC_URL = STATIC_URL_PROD
    DATABASES = {
        'default': DATABASE_PRODUCTION
    }
    CORS_ORIGIN_WHITELIST = [
        "https://abacusinventory.appspot.com",
        "https://api.abacus.dental",
    ]
    CORS_ALLOW_HEADERS = list(default_headers) + [
        'x-api-key',
    ]
else:
    DEBUG = True
    STATIC_URL = STATIC_URL_DEV
    SECURE_SSL_REDIRECT = False
    DATABASES = {'default': DATABASE_DEV}
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_HEADERS = list(default_headers) + [
        'x-api-key',
    ]
