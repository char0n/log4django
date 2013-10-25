# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'LogRecord.request_id'
        db.add_column(u'log4django_logrecord', 'request_id',
                      self.gf('django.db.models.fields.CharField')(db_index=True, max_length=36, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'LogRecord.request_id'
        db.delete_column(u'log4django_logrecord', 'request_id')


    models = {
        u'log4django.app': {
            'Meta': {'ordering': "('name',)", 'object_name': 'App'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'default': "'b3bf8fef-97bc-460b-a4ed-8848bfb3807e'", 'unique': 'True', 'max_length': '36'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'log4django.logrecord': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'LogRecord'},
            '_extra': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'app': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'records'", 'to': u"orm['log4django.App']"}),
            'exception_message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'exception_traceback': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fileName': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'lineNumber': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'loggerName': ('django.db.models.fields.CharField', [], {'max_length': '225'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'request_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'thread': ('django.db.models.fields.CharField', [], {'max_length': '225', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['log4django']
