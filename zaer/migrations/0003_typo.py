# Generated by Django 2.0.6 on 2018-08-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zaer', '0002_datetime to date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zaer',
            name='out_datetima',
        ),
        migrations.AddField(
            model_name='zaer',
            name='out_datetime',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
