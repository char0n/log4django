from django.utils.importlib import import_module

from tastypie.authorization import Authorization
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.resources import ModelResource
from tastypie import fields

from ..models import LogRecord
from ..settings import PERSISTATION_PIPELINE
from .authentication import AppAuthentication


class LogRecordResource(ModelResource):

    extra = fields.CharField(attribute='_extra', blank=True, default='{}')

    def save(self, bundle, skip_errors=False):
        self.is_valid(bundle)
        if bundle.errors and not skip_errors:
            raise ImmediateHttpResponse(response=self.error_response(bundle.request, bundle.errors))
        self.authorized_create_detail(self.get_object_list(bundle.request), bundle)
        for pipeline in PERSISTATION_PIPELINE:
            module_str, authenticator_str = pipeline.rsplit('.', 1)
            module = import_module(module_str)
            persistor = getattr(module, authenticator_str)
            persistor(bundle.data)
        return bundle

    def hydrate(self, bundle):
        bundle.data['app_id'] = self._meta.authentication.get_app(bundle.request).pk
        return bundle

    def build_schema(self):
        schema = super(LogRecordResource, self).build_schema()
        schema['CONSTANTS'] = {
            'LEVEL': LogRecord.LEVEL._choices
        }
        return schema

    class Meta:
        excludes = ['_extra']
        list_allowed_methods = ['post']
        detail_allowed_methods = []
        queryset = LogRecord.objects.all()
        authentication = AppAuthentication()
        authorization = Authorization()