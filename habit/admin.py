from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('pk', 'creator', 'place', 'time', 'action', 'is_useful', 'associated_habit', 'frequency', 'reward', 'is_public')
    list_filter = ('creator',)
    #search_fields = ('title', 'description',)

    def time_display(self, obj):
        return obj.time.strftime("%B %d, %Y %HH:%M:%S")
