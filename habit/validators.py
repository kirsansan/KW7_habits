from rest_framework import serializers
from rest_framework.exceptions import ValidationError

# from config.config import ALLOWED_LINKS


# class AllowedLinksValidator:
#
#     def __init__(self, field):
#         self.field = field
#
#     def __call__(self, value):
#         """if value is not include in allowed links (see config.config) we will raise ValidationError"""
#         tmp_value = dict(value).get(self.field)
#         if tmp_value:
#             for allowed in ALLOWED_LINKS:
#                 if allowed in tmp_value.lower():
#                     break
#             else:
#                 raise ValidationError(f"prohibited link detected - {tmp_value}")

class HabitMassValidator:

    def __init__(self, fields):
        self.fields = fields


    def __call__(self, object):
        """Validate all fields in a given """

        if self.fields.get('associated_habit') and self.fields.get('reward'):
            raise ValidationError('You must specify associated habit or reward. Not both at the same time')
