# Generated by Django 5.2.1 on 2025-06-04 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='bfile',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
