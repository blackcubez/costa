# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('requesterName', models.CharField(max_length=50)),
                ('requestDate', models.DateTimeField(auto_now=True)),
                ('lastUpdate', models.DateTimeField(auto_now_add=True)),
                ('requesterEmail', models.EmailField(max_length=254)),
                ('requestedEmail', models.EmailField(max_length=254)),
                ('comment', models.CharField(max_length=300)),
            ],
        ),
    ]
