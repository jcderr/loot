# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hoard'
        db.create_table(u'elections_hoard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('finalized', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('picks', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'elections', ['Hoard'])

        # Adding field 'Loot.conflict'
        db.add_column(u'elections_loot', 'conflict',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Loot.hoard'
        db.add_column(u'elections_loot', 'hoard',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elections.Hoard'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Hoard'
        db.delete_table(u'elections_hoard')

        # Deleting field 'Loot.conflict'
        db.delete_column(u'elections_loot', 'conflict')

        # Deleting field 'Loot.hoard'
        db.delete_column(u'elections_loot', 'hoard_id')


    models = {
        u'elections.election': {
            'Meta': {'object_name': 'Election'},
            'awarded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['elections.Loot']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['elections.Player']", 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        u'elections.hoard': {
            'Meta': {'object_name': 'Hoard'},
            'finalized': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'picks': ('django.db.models.fields.IntegerField', [], {})
        },
        u'elections.loot': {
            'Meta': {'object_name': 'Loot'},
            'bonus': ('django.db.models.fields.IntegerField', [], {}),
            'conflict': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hoard': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['elections.Hoard']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loot_type': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['elections.Player']", 'null': 'True', 'blank': 'True'})
        },
        u'elections.player': {
            'Meta': {'object_name': 'Player'},
            'character': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        }
    }

    complete_apps = ['elections']