# Generated by Django 3.2.12 on 2023-02-20 07:39

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cultures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Farmers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Seasons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Plots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contour', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('seasons', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=100)),
                ('culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agro.cultures')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agro.farmers')),
            ],
        ),
    ]