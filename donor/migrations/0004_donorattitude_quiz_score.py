# Generated by Django 3.2.6 on 2021-10-03 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0003_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='donorattitude',
            name='quiz_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
