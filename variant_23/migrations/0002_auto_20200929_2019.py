# Generated by Django 3.1.1 on 2020-09-29 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('variant_23', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='RATING',
        ),
        migrations.RemoveField(
            model_name='customers',
            name='SNUM',
        ),
    ]
