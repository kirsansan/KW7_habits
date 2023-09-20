from django.db import models
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    """Habit model"""
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='creator', **NULLABLE)
    title = models.CharField(max_length=150, verbose_name='title')
    place = models.CharField(max_length=150, verbose_name='place')
    time = models.TimeField(verbose_name='time for action')
    action = models.CharField(max_length=150, verbose_name='habit action')
    is_useful = models.BooleanField(default=True, verbose_name='is useful flag')
    associated_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='link to other habit')
    frequency = models.IntegerField(default=1, verbose_name='frequency by days')
    reward = models.CharField(max_length=150, verbose_name='reward', **NULLABLE)
    time_for_action = models.TimeField(verbose_name='action duration', **NULLABLE)
    is_public = models.BooleanField(default=True, verbose_name='is public flag')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'habit'
        verbose_name_plural = 'habits'
        ordering = ['pk']
