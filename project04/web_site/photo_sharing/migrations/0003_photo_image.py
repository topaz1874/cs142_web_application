# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo_sharing', '0002_user_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
