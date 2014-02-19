from django.conf import settings as django_settings


PAGE_TITLE = getattr(django_settings, 'LOG4DJANGO_PAGE_TITLE', 'log4django')
CONNECTION_NAME = getattr(django_settings, 'LOG4DJANGO_CONNECTION_NAME', 'default')
DEFAULT_APP_ID = getattr(django_settings, 'LOG4DJANGO_DEFAULT_APP_ID', None)
GERMAN_TASK_NAME = getattr(django_settings, 'LOG4DJANGO_GEARMAN_TASK_NAME', 'log4django_event')
PAGE_SIZE = getattr(django_settings, 'LOG4DJANGO_PAGE_SIZE', 100)
PAGINATOR_RANGE = getattr(django_settings, 'LOG4DJANGO_PAGINATOR_RANGE', 15)
EXTRA_DATA_INDENT = getattr(django_settings, 'LOG4DJANGO_EXTRA_DATA_INDENT', 4)
AUTHENTICATION_PIPELINE = getattr(django_settings, 'LOG4DJANGO_AUTHENTICATION_PIPELINE', (
    'log4django.pipeline.authentication.is_logged',
))
PERSISTATION_PIPELINE = getattr(django_settings, 'LOG4DJANGO_PERSISTATION_PIPELINE', (
    'log4django.pipeline.process_bundle_data.persist_record',
))
CSV_EXPORT_EXTRA_JSON_PATHS = getattr(django_settings, 'LOG4DJANGO_CSV_EXPORT_EXTRA_JSON_PATHS', tuple())
CSV_DOWNLOAD_FILE_NAME = getattr(django_settings, 'LOG4DJANGO_CSV_DOWNLOAD_FILE_NAME', 'log4django.csv')
COMMAND_EXCEPTION_CALLBACK = getattr(django_settings, 'LOG4DJANGO_COMMAND_EXCEPTION_CALLBACK', 'log4django.callbacks.exception_callback')
