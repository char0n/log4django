log4django
==========

log4django is full features logging platform for django applications.
The project is in very early stage, so excuse the brief documentation.

Requirements
------------

- python 2.7
- packages listed in setup.py

Installation
------------

Install via pipy or copy this module into your project or into your PYTHON_PATH.

In your `settings.py` file:


**Add log4django into INSTALLED_APPS.**
::

 INSTALLED_APPS = (
     'django.contrib.auth',
     'django.contrib.contenttypes',
     'django.contrib.sessions',
     'django.contrib.sites',
     'django.contrib.admin',
     'django.contrib.sitemaps',
     'debug_toolbar',
     'log4django'
 )

**Add log4django INTO CONTEXT_PROCESSORS.**
::

 TEMPLATE_CONTEXT_PROCESSORS = (
     'django.contrib.auth.context_processors.auth',
     'django.core.context_processors.debug',
     'django.core.context_processors.i18n',
     'django.core.context_processors.media',
     'django.core.context_processors.static',
     'django.core.context_processors.tz',
     'django.core.context_processors.request',
     'django.contrib.messages.context_processors.messages',
     'log4django.context_processors.log4django'
 )

**Configure your logging with log4django appender.**
::

 LOGGING = {
     'version': 1,
     'disable_existing_loggers': False,
     'handlers': {
         'log4django': {
             'level': 'DEBUG',
             'class': 'log4django.handlers.ModelHandler' # Synchronous log creations.
         },
         'log4django_async': {
             'level': 'DEBUG',
             'class': 'log4django.handlers.GearmanHandler' # Asynchronous log creations, doesn't block.
         }
     },
     'loggers': {
         '': {
             'handlers': ['log4django_async'],
             'level': 'DEBUG'
         }
     }
 }

Configuration
-------------

**django settings.py constants with default values.**

::

 LOG4DJANGO_PAGE_TITLE = 'log4django'
 LOG4DJANGO_CONNECTION_NAME = 'default'
 LOG4DJANGO_DEFAULT_APP_ID = None  # If you have only one app, put App.pk here
 LOG4DJANGO_GEARMAN_TASK_NAME = 'log4django_event'
 LOG4DJANGO_PAGE_SIZE = 100  # How many records to display on one page.
 LOG4DJANGO_PAGINATOR_RANGE = 15  # How many pages to show in pagination.
 LOG4DJANGO_EXTRA_DATA_INDENT = 4  # Extra data json indentation.
 LOG4DJANGO_AUTHENTICATION_PIPELINE', (
     'log4django.pipeline.authentication.is_logged',
 ))  # Basic authentication
 'LOG4DJANGO_PERSISTATION_PIPELINE', (
     'log4django.pipeline.process_bundle_data.persist_record',
 ))  # Controlls how records are persisted.
 LOG4DJANGO_CSV_EXPORT_EXTRA_JSON_PATHS = tuple()  #  List of json paths to include in csv export.
 LOG4DJANGO_CSV_DOWNLOAD_FILE_NAME = 'log4django.csv'


**Running asynchronously**

Asynchronous queue is managed by gearman job server (http://gearman.org/). In your logging config use
`log4django.handlers.GearmanHandler` as handler class. This way web request threads are not blocked by overhead
of saving a lots of log records to your database backend, but are sent to asynchronous queue insted.
You will also have to run management command that acts as gearman worker, pops log records from queue
and saves log records to database asynchronously.

::

 $ python manage.py log4django


Development setup
-----------------
::

 $ ./scripts/setup.sh
 $ python manage.py syncdb --noinput
 $ python manage.py test log4django
 $ python manage.py runserver


Tests
-----

**Tested on evnironment**

- Linux Mint 15 Olivia 64-bit
- python 2.7.4
- python unitest

**Running tests**

To run the tests, execute one of the following command:::

 $ python manage.py test log4django


Author
------

| char0n (Vladimir Gorej, CodeScale)
| email: gorej@codescale.net
| web: http://www.codescale.net/