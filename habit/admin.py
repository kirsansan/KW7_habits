from django.contrib import admin
from habit.models import Habit, SenderDailyLog


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('pk', 'creator', 'place', 'time', 'action',
                    'time_for_action', 'is_useful', 'associated_habit',
                    'frequency', 'reward', 'is_public')
    list_filter = ('creator',)

    def time_display(self, obj):
        return obj.time.strftime("%HH:%M:%S")


@admin.register(SenderDailyLog)
class LogAdmin(admin.ModelAdmin):
    list_display = ('habit_id', 'daily_status')
