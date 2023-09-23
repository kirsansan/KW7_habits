from datetime import time

from rest_framework.exceptions import ValidationError


class HabitActionTimeValidator:
    """validate time for action (less 2 minutes)"""

    def __init__(self, field):
        self.field = field

    def __call__(self, obj):
        """Validate time_for_action field in a given """
        if dict(obj).get(self.field):
            if dict(obj).get(self.field) > time(00, 2):
                raise ValidationError('time_for_action must be less 2 minutes ')


def habit_mass_validator(value):
    """Validate all fields in a given (w/o time_for_action)"""
    # print(value)
    if value.get('associated_habit') and value.get('reward'):  # both exist
        raise ValidationError('You must specify associated habit or reward. Not both at the same time')
    if value.get('associated_habit'):
        if not value.get('associated_habit').is_useful:  # associated is useless
            raise ValidationError('Associated habit must have is_useful flag as True')
    if value.get('is_useful') or 'is_useful' not in value:  # useful of default
        if value.get('reward'):
            raise ValidationError('Useful habit must not have reward')
        if value.get('associated_habit'):
            raise ValidationError('Useful habit must not have associated habit')
    if value.get('frequency'):  # exist
        if value.get('frequency') > 7:
            raise ValidationError('frequency of habit must be less 7 days')
