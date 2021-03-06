# Generated by Django 3.2 on 2021-05-01 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_alter_feedsource_last_refreshed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedentry',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.feedsource'),
        ),
        migrations.AlterField(
            model_name='feedsource',
            name='feed_url',
            field=models.URLField(max_length=2000, unique=True),
        ),
        migrations.AlterField(
            model_name='feedsource',
            name='name',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
