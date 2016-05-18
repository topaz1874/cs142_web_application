# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo_sharing', '0004_auto_20160510_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file_name',
            field=models.CharField(max_length=256),
        ),
    ]
