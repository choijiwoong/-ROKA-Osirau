# Generated by Django 3.2.4 on 2021-07-13 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0005_auto_20210703_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('dis_identify_num', models.CharField(max_length=14)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('identify_num', models.CharField(max_length=14)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
    ]
