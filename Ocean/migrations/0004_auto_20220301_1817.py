# Generated by Django 3.1.2 on 2022-03-01 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ocean', '0003_auto_20220301_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ocean',
            name='accession',
        ),
        migrations.RemoveField(
            model_name='ocean',
            name='releasedate',
        ),
    ]
