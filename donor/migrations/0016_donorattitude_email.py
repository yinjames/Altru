# Generated by Django 3.2.6 on 2021-10-08 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0015_rename_why_consent_donorattitude_consent_msg'),
    ]

    operations = [
        migrations.AddField(
            model_name='donorattitude',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
