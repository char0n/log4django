import codecs
import StringIO

from django.utils.importlib import import_module
csv = import_module('csv')

import jsonpath

from ..settings import CSV_EXPORT_EXTRA_JSON_PATHS


class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = StringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([unicode(s).encode("utf-8") if s is not None else u'' for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


class Export(object):
    def __init__(self, queryset):
        self.queryset = queryset
        self.buffer = StringIO.StringIO()
        self.writer = UnicodeWriter(self.buffer)

    def render(self):
        for logrecord in self.queryset:
            row = [logrecord.app, logrecord.loggerName, logrecord.get_level_display(), logrecord.timestamp,
                   logrecord.message, logrecord.fileName, logrecord.lineNumber, logrecord.thread,
                   logrecord.exception_message]
            for json_path in CSV_EXPORT_EXTRA_JSON_PATHS:
                jsonpath_result = jsonpath.jsonpath(logrecord.extra, json_path)
                row.append(jsonpath_result[0] if jsonpath_result is not False else u'')
            self.writer.writerow(row)
        csv_data = self.buffer.getvalue()
        self.buffer.close()
        return csv_data
