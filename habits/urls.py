from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.apps import HabitsConfig
from habits.views import (HabitListAPIView, PublicHabitListAPIView, HabitRetrieveAPIView, HabitCreateAPIView,
                          HabitDestroyAPIView, HabitUpdateAPIView)

app_name = HabitsConfig.name

router = DefaultRouter()

urlpatterns = [
    path(' ', HabitListAPIView.as_view(), name='habits_list'),
    path('public/', PublicHabitListAPIView.as_view(), name='public_habits_list'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='habits_retrieve'),
    path('create/', HabitCreateAPIView.as_view(), name='habits_create'),
    path('<int:pk>/delete/', HabitDestroyAPIView.as_view(), name='habits_delete'),
    path('<int:pk>/update/', HabitUpdateAPIView.as_view(), name='habits_update'),
]
