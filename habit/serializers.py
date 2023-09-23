from rest_framework import serializers

from habit.models import Habit
from habit.validators import HabitActionTimeValidator, habit_mass_validator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [habit_mass_validator,
                      HabitActionTimeValidator(field='time_for_action'), ]


class HabitPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
