# Generated by Django 2.1.1 on 2018-10-01 07:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zaer', '0006_no image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zaer',
            name='address',
            field=models.CharField(blank=True, max_length=1000, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='zaer',
            name='age',
            field=models.IntegerField(default=0, verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='zaer',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='zaer',
            name='gender',
            field=models.CharField(choices=[('m', 'مرد'), ('f', 'زن')], default='m', max_length=1, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='zaer',
            name='image',
            field=models.ImageField(blank=True, default='no_image', upload_to='images/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='zaer',
            name='in_datetime',
            field=models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now, verbose_name='in date'),
        ),
        migrations.AlterField(
            model_name='zaer',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='zaer',
            name='mobile',
            field=models.CharField(blank=True, max_length=16, verbose_name='mobile'),
        ),
        migrations.AlterField(
            model_name='zaer',
            name='out_datetime',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='out date'),
        ),
    ]
