from ..models import LogRecord


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