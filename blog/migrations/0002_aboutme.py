# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('dateMe', models.DateField(auto_created=True)),
                ('titleMe', models.CharField(max_length=20)),
                ('contentMe', models.TextField()),
            ],
        ),
    ]
