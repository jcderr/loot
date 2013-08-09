# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table(u'elections_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('character', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'elections', ['Player'])

        # Adding model 'Loot'
        db.create_table(u'elections_loot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('loot_type', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('bonus', self.gf('django.db.models.fields.IntegerField')()),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elections.Player'], null=True, blank=True)),
        ))
        db.send_create_signal(u'elections', ['Loot'])

        # Adding model 'Election'
        db.create_table(u'elections_election', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elections.Player'], null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
            ('loot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['elections.Loot'])),
            ('awarded', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'elections', ['Election'])


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table(u'elections_player')

        # Deleting model 'Loot'
        db.delete_table(u'elections_loot')

        # Deleting model 'Election'
        db.delete_table(u'elections_election')


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
        u'elections.loot': {
            'Meta': {'object_name': 'Loot'},
            'bonus': ('django.db.models.fields.IntegerField', [], {}),
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