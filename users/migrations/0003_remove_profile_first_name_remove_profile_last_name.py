# Generated by Django 5.0 on 2023-12-27 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_transaction_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
