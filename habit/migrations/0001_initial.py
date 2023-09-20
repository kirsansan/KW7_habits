# Generated by Django 4.2.5 on 2023-09-20 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('place', models.CharField(max_length=150, verbose_name='place')),
                ('time', models.DateTimeField(verbose_name='datetime for action')),
                ('action', models.CharField(max_length=150, verbose_name='habit action')),
                ('is_useful', models.BooleanField(default=True, verbose_name='is useful flag')),
                ('frequency', models.IntegerField(default=1, verbose_name='frequency by days')),
                ('reward', models.CharField(blank=True, max_length=150, null=True, verbose_name='reward')),
                ('time_for_action', models.TimeField(blank=True, null=True, verbose_name='action timing')),
                ('is_public', models.BooleanField(default=True, verbose_name='is public flag')),
                ('associated_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habit.habit', verbose_name='link to other habit')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='creator')),
            ],
            options={
                'verbose_name': 'habit',
                'verbose_name_plural': 'habits',
                'ordering': ['pk'],
            },
        ),
    ]
