from django.urls import path
from rest_framework import routers

from habit.apps import HabitConfig
from habit.views import HabitAPIView

app_name = HabitConfig.name

urlpatterns = [
    # habits


    path('', HabitAPIView.as_view()),
    # path('lesson/create/', LessonCreateAPIView.as_view()),
    # path('lesson/delete/<int:pk>/', LessonDeleteAPIView.as_view()),
    # path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view()),
    # path('lesson/detail/<int:pk>/', LessonDetailAPIView.as_view()),

]

# router = routers.SimpleRouter()
# router.register('course', CourseViewSet)
#
# urlpatterns += router.urls
