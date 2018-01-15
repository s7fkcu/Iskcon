# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MessageFile'
        db.create_table('conference_messagefile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['conference.Message'])),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=500)),
        ))
        db.send_create_signal('conference', ['MessageFile'])

        # Deleting field 'Group.is_enable_comments'
        db.delete_column('conference_group', 'is_enable_comments')

        # Deleting field 'Message.rght'
        db.delete_column('conference_message', 'rght')

        # Deleting field 'Message.parent'
        db.delete_column('conference_message', 'parent_id')

        # Deleting field 'Message.level'
        db.delete_column('conference_message', 'level')

        # Deleting field 'Message.lft'
        db.delete_column('conference_message', 'lft')

        # Deleting field 'Message.file'
        db.delete_column('conference_message', 'file')

        # Deleting field 'Message.tree_id'
        db.delete_column('conference_message', 'tree_id')


    def backwards(self, orm):
        # Deleting model 'MessageFile'
        db.delete_table('conference_messagefile')

        # Adding field 'Group.is_enable_comments'
        db.add_column('conference_group', 'is_enable_comments',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Message.rght'
        db.add_column('conference_message', 'rght',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)

        # Adding field 'Message.parent'
        db.add_column('conference_message', 'parent',
                      self.gf('mptt.fields.TreeForeignKey')(to=orm['conference.Message'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Message.level'
        db.add_column('conference_message', 'level',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)

        # Adding field 'Message.lft'
        db.add_column('conference_message', 'lft',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)

        # Adding field 'Message.file'
        db.add_column('conference_message', 'file',
                      self.gf('django.db.models.fields.files.FileField')(default=1, max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'Message.tree_id'
        db.add_column('conference_message', 'tree_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'conference.ban': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Ban'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_ban_end': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'conference.category': {
            'Meta': {'ordering': "['sort', 'title']", 'object_name': 'Category'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'conference.conferenceprofile': {
            'Meta': {'object_name': 'ConferenceProfile'},
            'dub_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_trusted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'one_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'server_email_login': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'server_email_passw': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'conference_profile'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['auth.User']"})
        },
        'conference.group': {
            'Meta': {'ordering': "['sort', 'title']", 'object_name': 'Group'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conference.Category']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('redactor.fields.RedactorField', [], {'max_length': '10000', 'blank': 'True'}),
            'email_sign': ('redactor.fields.RedactorField', [], {'max_length': '1000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_behalf_author': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_delete_server_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_moderate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_moderate_unregistered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_visibility_all_users': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_visible_members': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'leaders': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'leaders_group_rel'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'lifetime': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'perm': ('django.db.models.fields.IntegerField', [], {}),
            'server_email_login': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'server_email_passw': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'users_group_rel'", 'blank': 'True', 'through': "orm['conference.GroupUserRel']", 'to': "orm['auth.User']"})
        },
        'conference.groupuserrel': {
            'Meta': {'ordering': "['user__first_name', 'user__last_name', 'user__username']", 'unique_together': "(('group', 'user'),)", 'object_name': 'GroupUserRel'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_ban_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conference.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_frozen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'conference.message': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Message'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conference.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_moderate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'recipients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.User']", 'null': 'True', 'through': "orm['conference.MessageRecipientRel']", 'blank': 'True'}),
            'text': ('redactor.fields.RedactorField', [], {'max_length': '10000'}),
            'theme': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_message_rel'", 'to': "orm['auth.User']"})
        },
        'conference.messagefile': {
            'Meta': {'object_name': 'MessageFile'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conference.Message']"})
        },
        'conference.messagerecipientrel': {
            'Meta': {'ordering': "['-id']", 'object_name': 'MessageRecipientRel'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_removed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_sent_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_recipient_rel'", 'to': "orm['conference.Message']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_recipient_rel'", 'to': "orm['auth.User']"})
        },
        'conference.messagerequest': {
            'Meta': {'ordering': "['-created']", 'object_name': 'MessageRequest'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conference.Group']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'theme': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['conference']