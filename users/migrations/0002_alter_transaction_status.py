# Generated by Django 5.0 on 2023-12-24 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('hidden', 'hidden'), ('credit', 'credit'), ('processing', 'processing'), ('confirming', 'confirming'), ('error', 'error'), ('failed', 'failed')], max_length=15),
        ),
    ]
