# Generated by Django 4.2.3 on 2023-08-01 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
