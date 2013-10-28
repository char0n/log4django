#!/bin/sh

SETTINGS='settings.py'
cat > $SETTINGS <<EOF
DEBUG = True

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test.db',
    },
}

MIDDLEWARE_CLASSES = (
    'log_request_id.middleware.RequestIDMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'log4django',
    'south',
)

STATIC_URL = '/static/'

SECRET_KEY = 'secret_key'
ROOT_URLCONF = 'global_urls'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        '': {
            'handlers': ['null'],
            'level': 'DEBUG'
        }
    }
}

EOF

URLS='global_urls.py'
cat > $URLS <<EOF
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', include('log4django.urls', namespace='log4django', app_name='log4django')),
)

EOF

export PYTHONPATH=.
export DJANGO_SETTINGS_MODULE=settings