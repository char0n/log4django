from . import settings


def log4django(request):
    return {
        'PAGE_TITLE': settings.PAGE_TITLE
    }