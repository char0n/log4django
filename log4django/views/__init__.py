from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_GET

from ..models import LogRecord, App
from ..settings import PAGE_SIZE
from ..decorators import authenticate


@authenticate()
@require_GET
def main_screen(request):
    logrecord_qs = _filter_records(request)
    paginator = Paginator(logrecord_qs, PAGE_SIZE)
    page = request.GET.get('page', None)
    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        records = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        records = paginator.page(paginator.num_pages)
    # Getting filtering values.
    apps = App.objects.all()
    try:
        loggers = list(LogRecord.objects.distinct('loggerName').order_by('loggerName').values('loggerName'))
    except NotImplementedError:
        loggers = set(LogRecord.objects.order_by('loggerName').values('loggerName'))
    levels = LogRecord.LEVEL
    return render_to_response('log4django/bootstrap/base.html', RequestContext(request, dict(
        records=records, apps=apps, loggers=loggers, levels=levels,
        filter_levels=[int(l) for l in request.GET.getlist('level')]
    )))


def _filter_records(request):
    getvars = request.GET
    logrecord_qs = LogRecord.objects.all().select_related('app')
    # Filtering by get params.
    if getvars.get('app'):
        logrecord_qs = logrecord_qs.filter(app_id=getvars.get('app'))
    if getvars.get('logger'):
        logrecord_qs = logrecord_qs.filter(loggerName=getvars.get('logger'))
    if getvars.getlist('level'):
        logrecord_qs = logrecord_qs.filter(level__in=getvars.getlist('level'))
    if getvars.get('from'):
        logrecord_qs = logrecord_qs.filter(timestamp__gte=getvars.get('from'))
    if getvars.get('to'):
        logrecord_qs = logrecord_qs.filter(timestamp__lte=getvars.get('to'))
    return logrecord_qs