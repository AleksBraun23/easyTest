# Generated by Django 2.1.2 on 2018-11-04 14:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20181102_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='time',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, verbose_name='time for test'),
        ),
    ]
