# Generated by Django 5.2.1 on 2025-05-26 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuscore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuscore',
            name='avg',
            field=models.IntegerField(default=0),
        ),
    ]
