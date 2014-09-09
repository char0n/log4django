# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'LogRecord.app'
        db.alter_column(u'log4django_logrecord', 'app_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['log4django.App']))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'LogRecord.app'
        raise RuntimeError("Cannot reverse this migration. 'LogRecord.app' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'LogRecord.app'
        db.alter_column(u'log4django_logrecord', 'app_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['log4django.App']))

    models = {
        u'log4django.app': {
            'Meta': {'ordering': "('name',)", 'object_name': 'App'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'default': "'3302a266-0bb2-434c-8dd9-c73a5c524ad1'", 'unique': 'True', 'max_length': '36'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'log4django.logrecord': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'LogRecord'},
            '_extra': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'app': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'records'", 'null': 'True', 'to': u"orm['log4django.App']"}),
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