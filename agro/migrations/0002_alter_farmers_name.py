# Generated by Django 3.2.12 on 2023-02-20 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmers',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
