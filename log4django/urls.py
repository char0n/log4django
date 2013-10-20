from django.conf.urls import patterns, include, url

from tastypie.api import Api

from .api.resources import LogRecordResource


api_patterns = Api(api_name='v1')
api_patterns.register(LogRecordResource())


urlpatterns = patterns('log4django.views',
    url(r'^api/', include(api_patterns.urls)),
    url(r'^export/csv/$', 'exports.csv', name='csv_export'),
    url(r'^$', 'main_screen', name='main_screen'),
)