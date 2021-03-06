# Generated by Django 3.2.4 on 2021-06-27 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting_location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('location', models.CharField(default='', max_length=50)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Servicer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('location', models.CharField(default='', max_length=50)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('location', models.CharField(default='', max_length=50)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
            ],
        ),
    ]
