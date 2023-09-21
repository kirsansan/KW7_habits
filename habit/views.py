from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit, SenderDailyLog
from habit.paginators import AllListsPaginator
from habit.permissions import IsOwner, IsAdministrator, IsModerator
from habit.serializers import HabitSerializer


class HabitPublicAPIView(ListAPIView):
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
            print("You are not allowed to public")
            return Habit.objects.filter(is_public=True)


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


class HabitDetailAPIView(RetrieveAPIView):
    """Habit detail view"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsAdministrator]


class HabitDeleteAPIView(DestroyAPIView):
    """Habit delete"""
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdministrator]


class HabitCreateAPIView(CreateAPIView):
    """Habit create"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """save owner(creator) of Habit"""
        new_habit = serializer.save()
        new_habit.creator = self.request.user
        new_habit.save()
        new_log = SenderDailyLog(habit_id=new_habit, daily_status=SenderDailyLog.CREATE)
        new_log.save()


class HabitUpdateAPIView(UpdateAPIView):
    """Habit update"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsModerator | IsAdministrator]
