# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('file_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(to='photo_sharing.User'),
        ),
        migrations.AddField(
            model_name='comments',
            name='photo',
            field=models.ForeignKey(to='photo_sharing.Photo'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(to='photo_sharing.User'),
        ),
    ]
