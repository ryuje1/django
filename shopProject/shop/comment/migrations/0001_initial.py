# Generated by Django 5.2.1 on 2025-06-20 08:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0002_alter_customer_bfile_alter_customer_bfile2'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('cno', models.AutoField(primary_key=True, serialize=False)),
                ('cpw', models.CharField(blank=True, max_length=20, null=True)),
                ('ccontent', models.TextField(blank=True)),
                ('cdate', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='member.member')),
            ],
        ),
    ]
