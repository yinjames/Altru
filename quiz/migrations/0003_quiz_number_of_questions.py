# Generated by Django 3.2.5 on 2021-07-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_quiz_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='number_of_questions',
            field=models.IntegerField(default=5),
        ),
    ]
