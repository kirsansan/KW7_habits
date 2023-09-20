from rest_framework import serializers

from habit.models import Habit
from habit.validators import HabitMassValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        # validators = [AllowedLinksValidator(field='video_url')]
        validators = [HabitMassValidator]


class HabitPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        # validators = [AllowedLinksValidator(field='video_url')]
        validators = [HabitMassValidator]