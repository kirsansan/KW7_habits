from django.urls import path
from rest_framework import routers

from habit.apps import HabitConfig
from habit.views import HabitAPIView, HabitCreateAPIView, HabitDetailAPIView, HabitUpdateAPIView, HabitDeleteAPIView, \
    HabitPublicAPIView

app_name = HabitConfig.name

urlpatterns = [
    # habits

    path('all/', HabitPublicAPIView.as_view(), name='public habits listview'),
    path('my/', HabitAPIView.as_view(), name='my habits listview'),
    path('create/', HabitCreateAPIView.as_view(), name='create'),
    path('delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='delete'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='update'),
    path('detail/<int:pk>/', HabitDetailAPIView.as_view(), name='detail'),

]

# router = routers.SimpleRouter()
# router.register('course', CourseViewSet)
#
# urlpatterns += router.urls
