# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, b'Waiting'), (2, b'Approved'), (3, b'In progress'), (4, b'Completed'), (5, b'Rejected')]),
        ),
    ]
