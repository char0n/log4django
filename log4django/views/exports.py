from django.http import HttpResponse
from django.views.decorators.http import require_GET

from . import _filter_records
from ..exports.csv import Export as CsvExport
from ..decorators import authenticate
from ..settings import CSV_DOWNLOAD_FILE_NAME


@authenticate()
@require_GET
def csv(request):
    logrecords_qs = _filter_records(request)
    export = CsvExport(logrecords_qs)
    response = HttpResponse(export.render(), content_type='application/csv')
    response['Content-Disposition'] = 'attachment; filename="{0}"'.format(CSV_DOWNLOAD_FILE_NAME)
    return response