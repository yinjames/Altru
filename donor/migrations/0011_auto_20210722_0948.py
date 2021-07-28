# Generated by Django 3.2.5 on 2021-07-22 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0010_remove_donorknowledge_income_range'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorattitude',
            name='q1',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='donorattitude',
            name='q11',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='donorattitude',
            name='q12',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='donorattitude',
            name='q14',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='donorattitude',
            name='q3',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='donorknowledge',
            name='q1',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='donorknowledge',
            name='q10',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='donorknowledge',
            name='q3',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='donorknowledge',
            name='q4',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='donorknowledge',
            name='q5',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='donorknowledge',
            name='q6',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='donorknowledge',
            name='q7',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='donorknowledge',
            name='q8',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')]),
        ),
        migrations.AlterField(
            model_name='donorknowledge',
            name='q9',
            field=models.BooleanField(choices=[(0, 'No'), (1, 'Yes')]),
        ),
    ]