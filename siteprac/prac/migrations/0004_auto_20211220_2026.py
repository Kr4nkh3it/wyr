# Generated by Django 3.2.9 on 2021-12-21 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prac', '0003_auto_20211220_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice2',
            field=models.CharField(max_length=200),
        ),
    ]
