from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'dbempleado',
        'USER':'juan',
        'PASSWORD':'chiquita',
        'HOST':'localhost',
        'PORT':'5433',
    }
}


STATIC_URL = '/static/'
