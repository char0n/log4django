# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LogRecord'
        db.create_table(u'log4django_logrecord', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(related_name='records', to=orm['log4django.App'])),
            ('loggerName', self.gf('django.db.models.fields.CharField')(max_length=225)),
            ('level', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('fileName', self.gf('django.db.models.fields.TextField')()),
            ('lineNumber', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('thread', self.gf('django.db.models.fields.CharField')(max_length=225, null=True, blank=True)),
            ('exception_message', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('exception_traceback', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('_extra', self.gf('django.db.models.fields.TextField')(default='{}')),
        ))
        db.send_create_signal(u'log4django', ['LogRecord'])

        # Adding model 'App'
        db.create_table(u'log4django_app', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(default='9100f401-106f-433a-9f56-9a596dc9008e', unique=True, max_length=36)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'log4django', ['App'])


    def backwards(self, orm):
        # Deleting model 'LogRecord'
        db.delete_table(u'log4django_logrecord')

        # Deleting model 'App'
        db.delete_table(u'log4django_app')


    models = {
        u'log4django.app': {
            'Meta': {'ordering': "('name',)", 'object_name': 'App'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'default': "'6607271c-a797-4891-a5f9-9d9db8a71ac9'", 'unique': 'True', 'max_length': '36'}),
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
            'thread': ('django.db.models.fields.CharField', [], {'max_length': '225', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['log4django']