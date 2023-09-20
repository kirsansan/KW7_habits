from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.paginators import AllListsPaginator
from habit.serializers import HabitSerializer


class HabitAPIView(ListAPIView):
    """Habit list-view """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = AllListsPaginator

    def get_queryset(self):
        """ moderator have permission for view all habits, other users might see only own habits"""
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='moderator').exists():
            return Habit.objects.all()
        else:
            return Habit.objects.filter(creator=user)
