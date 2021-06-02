import os
from corsheaders.defaults import default_headers
from abacusinventory.config.database import DATABASE_DEV
ROOT_URLCONF = 'abacusinventory.urls'
WSGI_APPLICATION = 'abacusinventory.wsgi.application'
ASGI_APPLICATION = 'abacusinventory.asgi.application'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = ''
DEBUG = False
LOGGING_CONFIG = None  # Logging to allow for default use of CSG logger
LOCKDOWN_ADMIN = False

ALLOWED_HOSTS = [
    '*'
]

INSTALLED_APPS = [
    'api.config',
    'rest_framework',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'api',
    'corsheaders',
    'firebase_auth',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'firebase_auth.authentication.FirebaseAuthentication',
    ),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL_DEV = '/static/'
STATIC_URL_QA = 'https://storage.googleapis.com/abacusinventory-qa-static/'
STATIC_URL_STAGING = 'https://storage.googleapis.com/abacusinventory-staging-static/'
STATIC_URL_PROD = 'https://storage.googleapis.com/abacusinventory-static/'

DATABASES = {
    'default': DATABASE_DEV
}
CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "https://api.abacus.dental",
    "https://my.abacus.dental"
]
CORS_ALLOW_HEADERS = list(default_headers) + [
    'HTTP-AUTHORIZATION',
    'AUTHORIZATION',
    'Access-Control-Allow-Origin',
    'Access-Control-Allow-Methods',
    'Access-Control-Allow-Headers'

]
SECURE_SSL_REDIRECT = False
