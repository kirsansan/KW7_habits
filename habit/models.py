from django.db import models
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    """Habit model"""
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='creator', **NULLABLE)
    title = models.CharField(max_length=150, verbose_name='title')
    place = models.CharField(max_length=150, verbose_name='place')
    time = models.TimeField(verbose_name='start time')
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

class SenderDailyLog(models.Model):
    """Daily Log for sending
       this table must be created every day """
    SENT = 'SENT'
    ERROR = 'ERROR'
    CREATE = 'CREATE'

    STATUS = (
        (CREATE, 'create'),
        (SENT, 'sent'),
        (ERROR, 'sending error'),
    )

    habit_id = models.OneToOneField(Habit, default=1, verbose_name='habit id', on_delete=models.CASCADE, primary_key=True)
    daily_status = models.CharField(max_length=6, choices=STATUS, default=CREATE, verbose_name='sending status')

    def __str__(self):
        return f"{self.habit} have status {self.is_send}"

    class Meta:
        verbose_name = 'log status'
        verbose_name_plural = 'log statuses'
        ordering = ['pk']
