# Generated by Django 2.0.6 on 2018-08-07 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zaer', '0005_remove birth date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zaer',
            name='image',
            field=models.ImageField(blank=True, default='no_image', upload_to='images/'),
        ),
    ]