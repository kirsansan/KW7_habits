# Generated by Django 4.2.5 on 2023-09-21 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0005_remove_senderdailylog_habit_remove_senderdailylog_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(verbose_name='start time'),
        ),
    ]
