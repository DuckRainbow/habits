from rest_framework.serializers import ValidationError


class RewardValidator:

    def __init__(self, field1, field2):
        self.related_habit = field1
        self.reward = field2

    def __call__(self):
        """Исключаем одновременный выбор связанной привычки и указания вознаграждения."""
        if self.related_habit is not None and self.reward is not None:
            raise ValidationError('Привычка не может иметь одновременно и связанную привычку, и вознаграждение.')
        elif self.related_habit is None and self.reward is None:
            raise ValidationError('У привычки не может не быть связанной привычки или вознаграждения.')
        return None


class TimeValidator:

    def __init__(self, field):
        self.time_to_complete = field

    def __call__(self):
        """Проверяем, чтобы время выполнения было не больше 120 секунд."""
        if self.time_to_complete > 120:
            raise ValidationError('Время выполнения должно быть не больше 120 секунд.')


class RelatedHabitValidator:

    def __init__(self, field):
        self.related_habit = field

    def __call__(self):
        """Проверяем, чтобы в связанные привычки попадали только привычки с признаком приятной привычки."""
        if not self.related_habit.is_pleasant:
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')


class PleasantValidator:

    def __init__(self, field1, field2, field3):
        self.is_pleasant = field1
        self.related_habit = field2
        self.reward = field3

    def __call__(self):
        """Проверяем, чтобы у приятной привычки не было вознаграждения или связанной привычки."""
        if self.is_pleasant:
            if self.related_habit is not None or self.reward is not None:
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')


class RegularityHabitValidator:

    def __init__(self, field):
        self.regularity = field

    def __call__(self):
        """Проверяем, чтобы периодичность не была реже, чем 1 раз в неделю(7 дней)."""
        if not self.regularity > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')
