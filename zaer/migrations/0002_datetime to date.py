# Generated by Django 2.0.6 on 2018-08-05 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zaer', '0001_init'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zaer',
            old_name='in_date',
            new_name='in_datetime',
        ),
        migrations.RenameField(
            model_name='zaer',
            old_name='out_date',
            new_name='out_datetima',
        ),
        migrations.AlterField(
            model_name='zaer',
            name='birth_date',
            field=models.DateField(blank=True, db_index=True),
        ),
    ]
