from . import settings


def log4django(request):
    return {
        'LOG4DJANGO_PAGE_TITLE': settings.PAGE_TITLE
    }
