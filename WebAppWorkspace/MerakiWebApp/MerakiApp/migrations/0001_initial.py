# Generated by Django 2.2.17 on 2022-02-16 11:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('location_tag', models.CharField(default='', max_length=128)),
                ('device_type', models.CharField(max_length=128)),
                ('model', models.CharField(max_length=128)),
                ('serial', models.CharField(max_length=128, unique=True)),
                ('net_ID', models.CharField(max_length=128)),
                ('slug', models.SlugField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_ID', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('max_noise', models.IntegerField(default=0)),
                ('min_noise', models.IntegerField(default=0)),
                ('max_light', models.IntegerField(default=0)),
                ('min_light', models.IntegerField(default=0)),
                ('max_people', models.IntegerField(default=0)),
                ('min_people', models.IntegerField(default=0)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='StudySpace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('avg_noise_level', models.FloatField(default=0)),
                ('avg_light_level', models.FloatField(default=0)),
                ('people', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'StudySpaces',
            },
        ),
    ]
