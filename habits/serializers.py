from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from habits.models import Habit


class HabitsSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
