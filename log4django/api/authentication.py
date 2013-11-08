import logging

from django.core.cache import cache

from tastypie.authentication import Authentication
from tastypie.http import HttpUnauthorized

from ..models import App


log = logging.getLogger(__name__)


class AppAuthentication(Authentication):

    HEADER_NAME = 'HTTP_AUTHORIZATION'

    def is_authenticated(self, request, **kwargs):
        app_key = self.get_identifier(request)
        try:
            log.debug('Api authentication parsed credentials: %s', app_key)
            app = self.get_app(request)
        except (App.DoesNotExist, App.MultipleObjectsReturned):
            log.exception('Api authentication not successful.')
            return HttpUnauthorized()
        return isinstance(app, App)

    def get_identifier(self, request):
        app_key = request.GET.get('app_key') or request.POST.get('app_key')
        try:
            if not app_key and self.HEADER_NAME in request.META:
                log.debug('Api authentication header received: %s', request.META[self.HEADER_NAME])
                app_key = request.META[self.HEADER_NAME].split(':', 1)[1].strip()
        except IndexError:
            log.exception('Invalid Authorization header detected: %s', request.META[self.HEADER_NAME])
            return HttpUnauthorized()
        return app_key

    def get_app(self, request):
        app_key = self.get_identifier(request)
        cache_key = 'log4django__app_{0}'.format(app_key)
        app = cache.get(cache_key, None)
        if app is None:
            app = App.objects.get(key=app_key)
            cache.set(cache_key, app)
        return app