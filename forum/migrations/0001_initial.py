# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import forum.models.utils
import datetime
import forum.utils.time
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=39)),
                ('action_type', models.CharField(max_length=32)),
                ('action_date', models.DateTimeField(default=datetime.datetime.now)),
                ('extra', forum.models.utils.PickledObjectField(null=True, editable=False)),
                ('canceled', models.BooleanField(default=False)),
                ('canceled_at', models.DateTimeField(null=True)),
                ('canceled_ip', models.CharField(max_length=39)),
            ],
        ),
        migrations.CreateModel(
            name='ActionRepute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('value', models.IntegerField(default=0)),
                ('by_canceled', models.BooleanField(default=False)),
                ('action', models.ForeignKey(related_name='reputes', to='forum.Action')),
            ],
        ),
        migrations.CreateModel(
            name='AuthKeyUserAssociation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('provider', models.CharField(max_length=64)),
                ('added_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('awarded_at', models.DateTimeField(default=datetime.datetime.now)),
                ('action', models.OneToOneField(related_name='award', to='forum.Action')),
            ],
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.SmallIntegerField()),
                ('cls', models.CharField(max_length=50, null=True)),
                ('awarded_count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.CharField(max_length=300)),
                ('flagged_at', models.DateTimeField(default=datetime.datetime.now)),
                ('action', models.OneToOneField(related_name='flag', to='forum.Action')),
            ],
        ),
        migrations.CreateModel(
            name='KeyValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=255)),
                ('value', forum.models.utils.PickledObjectField(null=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='MarkedTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.CharField(max_length=16, choices=[(b'good', 'interesting'), (b'bad', 'ignored')])),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('tagnames', models.CharField(max_length=125)),
                ('body', models.TextField()),
                ('node_type', models.CharField(default=b'node', max_length=16)),
                ('added_at', models.DateTimeField(default=datetime.datetime.now)),
                ('score', models.IntegerField(default=0)),
                ('state_string', models.TextField(default=b'')),
                ('last_activity_at', models.DateTimeField(null=True, blank=True)),
                ('extra', forum.models.utils.PickledObjectField(null=True, editable=False)),
                ('extra_count', models.IntegerField(default=0)),
                ('marked', models.BooleanField(default=False)),
                ('abs_parent', models.ForeignKey(related_name='all_children', to='forum.Node', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NodeRevision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('tagnames', models.CharField(max_length=125)),
                ('body', models.TextField()),
                ('summary', models.CharField(max_length=300)),
                ('revision', models.PositiveIntegerField()),
                ('revised_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='NodeState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state_type', models.CharField(max_length=16)),
                ('action', models.OneToOneField(related_name='node_state', to='forum.Action')),
                ('node', models.ForeignKey(related_name='states', to='forum.Node')),
            ],
        ),
        migrations.CreateModel(
            name='OpenIdAssociation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_url', models.TextField(max_length=2047)),
                ('handle', models.CharField(max_length=255)),
                ('secret', models.TextField(max_length=255)),
                ('issued', models.IntegerField()),
                ('lifetime', models.IntegerField()),
                ('assoc_type', models.TextField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='OpenIdNonce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_url', models.URLField()),
                ('timestamp', models.IntegerField()),
                ('salt', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSubscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auto_subscription', models.BooleanField(default=True)),
                ('last_view', models.DateTimeField(default=datetime.datetime(2017, 6, 27, 3, 50, 53, 584697))),
                ('question', models.ForeignKey(to='forum.Node')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enable_notifications', models.BooleanField(default=True)),
                ('member_joins', models.CharField(default=b'n', max_length=1)),
                ('new_question', models.CharField(default=b'n', max_length=1)),
                ('new_question_watched_tags', models.CharField(default=b'i', max_length=1)),
                ('subscribed_questions', models.CharField(default=b'i', max_length=1)),
                ('all_questions', models.BooleanField(default=False)),
                ('all_questions_watched_tags', models.BooleanField(default=False)),
                ('questions_viewed', models.BooleanField(default=False)),
                ('notify_answers', models.BooleanField(default=True)),
                ('notify_reply_to_comments', models.BooleanField(default=True)),
                ('notify_comments_own_post', models.BooleanField(default=True)),
                ('notify_comments', models.BooleanField(default=False)),
                ('notify_accepted', models.BooleanField(default=False)),
                ('send_digest', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)),
                ('used_count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('-used_count', 'name'),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_approved', models.BooleanField(default=False)),
                ('email_isvalid', models.BooleanField(default=True)),
                ('reputation', models.IntegerField(default=0)),
                ('gold', models.PositiveIntegerField(default=0)),
                ('silver', models.PositiveIntegerField(default=0)),
                ('bronze', models.PositiveIntegerField(default=0)),
                ('last_seen', models.DateTimeField(default=datetime.datetime.now)),
                ('real_name', models.CharField(max_length=100, blank=True)),
                ('website', models.URLField(blank=True)),
                ('location', models.CharField(max_length=100, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('about', models.TextField(blank=True)),
                ('subscriptions', models.ManyToManyField(related_name='subscribers', through='forum.QuestionSubscription', to='forum.Node')),
            ],
            bases=('auth.user', models.Model),
        ),
        migrations.CreateModel(
            name='UserProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=16)),
                ('value', forum.models.utils.PickledObjectField(null=True, editable=False)),
                ('user', models.ForeignKey(related_name='properties', to='forum.User')),
            ],
        ),
        migrations.CreateModel(
            name='ValidationHash',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash_code', models.CharField(unique=True, max_length=255)),
                ('seed', models.CharField(max_length=12)),
                ('expiration', models.DateTimeField(default=forum.utils.time.one_day_from_now)),
                ('type', models.CharField(max_length=12)),
                ('user', models.ForeignKey(to='forum.User')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.SmallIntegerField()),
                ('voted_at', models.DateTimeField(default=datetime.datetime.now)),
                ('action', models.OneToOneField(related_name='vote', to='forum.Action')),
                ('node', models.ForeignKey(related_name='votes', to='forum.Node')),
                ('user', models.ForeignKey(related_name='votes', to='forum.User')),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='created_by',
            field=models.ForeignKey(related_name='created_tags', to='forum.User'),
        ),
        migrations.AddField(
            model_name='tag',
            name='marked_by',
            field=models.ManyToManyField(related_name='marked_tags', through='forum.MarkedTag', to='forum.User'),
        ),
        migrations.AddField(
            model_name='subscriptionsettings',
            name='user',
            field=models.OneToOneField(related_name='subscription_settings', editable=False, to='forum.User'),
        ),
        migrations.AddField(
            model_name='questionsubscription',
            name='user',
            field=models.ForeignKey(to='forum.User'),
        ),
        migrations.AddField(
            model_name='noderevision',
            name='author',
            field=models.ForeignKey(related_name='noderevisions', to='forum.User'),
        ),
        migrations.AddField(
            model_name='noderevision',
            name='node',
            field=models.ForeignKey(related_name='revisions', to='forum.Node'),
        ),
        migrations.AddField(
            model_name='node',
            name='active_revision',
            field=models.OneToOneField(related_name='active', null=True, to='forum.NodeRevision'),
        ),
        migrations.AddField(
            model_name='node',
            name='author',
            field=models.ForeignKey(related_name='nodes', to='forum.User'),
        ),
        migrations.AddField(
            model_name='node',
            name='extra_ref',
            field=models.ForeignKey(to='forum.Node', null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='last_activity_by',
            field=models.ForeignKey(to='forum.User', null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='last_edited',
            field=models.ForeignKey(related_name='edited_node', null=True, to='forum.Action', unique=True),
        ),
        migrations.AddField(
            model_name='node',
            name='parent',
            field=models.ForeignKey(related_name='children', to='forum.Node', null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='tags',
            field=models.ManyToManyField(related_name='nodes', to='forum.Tag'),
        ),
        migrations.AddField(
            model_name='markedtag',
            name='tag',
            field=models.ForeignKey(related_name='user_selections', to='forum.Tag'),
        ),
        migrations.AddField(
            model_name='markedtag',
            name='user',
            field=models.ForeignKey(related_name='tag_selections', to='forum.User'),
        ),
        migrations.AddField(
            model_name='flag',
            name='node',
            field=models.ForeignKey(related_name='flags', to='forum.Node'),
        ),
        migrations.AddField(
            model_name='flag',
            name='user',
            field=models.ForeignKey(related_name='flags', to='forum.User'),
        ),
        migrations.AddField(
            model_name='badge',
            name='awarded_to',
            field=models.ManyToManyField(related_name='badges', through='forum.Award', to='forum.User'),
        ),
        migrations.AddField(
            model_name='award',
            name='badge',
            field=models.ForeignKey(related_name='awards', to='forum.Badge'),
        ),
        migrations.AddField(
            model_name='award',
            name='node',
            field=models.ForeignKey(to='forum.Node', null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='trigger',
            field=models.ForeignKey(related_name='awards', to='forum.Action', null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='user',
            field=models.ForeignKey(to='forum.User'),
        ),
        migrations.AddField(
            model_name='authkeyuserassociation',
            name='user',
            field=models.ForeignKey(related_name='auth_keys', to='forum.User'),
        ),
        migrations.AddField(
            model_name='actionrepute',
            name='user',
            field=models.ForeignKey(related_name='reputes', to='forum.User'),
        ),
        migrations.AddField(
            model_name='action',
            name='canceled_by',
            field=models.ForeignKey(related_name='canceled_actions', to='forum.User', null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='node',
            field=models.ForeignKey(related_name='actions', to='forum.Node', null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='real_user',
            field=models.ForeignKey(related_name='proxied_actions', to='forum.User', null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='user',
            field=models.ForeignKey(related_name='actions', to='forum.User'),
        ),
        migrations.CreateModel(
            name='ActionProxy',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('forum.action',),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
            ],
            options={
                'abstract': False,
                'proxy': True,
            },
            bases=('forum.node',),
        ),
        migrations.CreateModel(
            name='AnswerRevision',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('forum.noderevision',),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
            ],
            options={
                'ordering': ('-added_at',),
                'abstract': False,
                'proxy': True,
            },
            bases=('forum.node',),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
            ],
            options={
                'abstract': False,
                'proxy': True,
            },
            bases=('forum.node',),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
            ],
            options={
                'abstract': False,
                'proxy': True,
            },
            bases=('forum.node',),
        ),
        migrations.CreateModel(
            name='QuestionRevision',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('forum.noderevision',),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('user', 'node')]),
        ),
        migrations.AlterUniqueTogether(
            name='validationhash',
            unique_together=set([('user', 'type')]),
        ),
        migrations.AlterUniqueTogether(
            name='userproperty',
            unique_together=set([('user', 'key')]),
        ),
        migrations.AlterUniqueTogether(
            name='nodestate',
            unique_together=set([('node', 'state_type')]),
        ),
        migrations.AlterUniqueTogether(
            name='noderevision',
            unique_together=set([('node', 'revision')]),
        ),
        migrations.AlterUniqueTogether(
            name='flag',
            unique_together=set([('user', 'node')]),
        ),
        migrations.AlterUniqueTogether(
            name='award',
            unique_together=set([('user', 'badge', 'node')]),
        ),
    ]
