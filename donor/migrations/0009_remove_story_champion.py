# Generated by Django 3.2.6 on 2021-10-04 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0008_donorattitude_consent_after_reward'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='champion',
        ),
    ]