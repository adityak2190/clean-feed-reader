# Generated by Django 3.1.3 on 2021-01-02 06:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedsummary',
            old_name='description',
            new_name='summary',
        ),
        migrations.AddField(
            model_name='feedsummary',
            name='author',
            field=models.CharField(default='admin', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedsummary',
            name='title_detail',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedsummary',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 6, 39, 40, 810612)),
            preserve_default=False,
        ),
    ]
