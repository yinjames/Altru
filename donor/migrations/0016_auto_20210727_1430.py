# Generated by Django 3.2.5 on 2021-07-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0015_auto_20210727_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorattitude',
            name='visitor_id',
            field=models.UUIDField(blank=True, editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='donorknowledge',
            name='visitor_id',
            field=models.UUIDField(blank=True, editable=False, null=True, unique=True),
        ),
    ]
