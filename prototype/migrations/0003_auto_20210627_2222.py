# Generated by Django 3.2.4 on 2021-06-27 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0002_auto_20210627_2207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meeting_location',
            options={'ordering': ['-location']},
        ),
        migrations.RemoveField(
            model_name='meeting_location',
            name='name',
        ),
    ]
