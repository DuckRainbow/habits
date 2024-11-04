from rest_framework.serializers import ValidationError


class RewardValidator:

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self):
        """Исключаем одновременный выбор связанной привычки и указания вознаграждения."""
        if self.field1 is not None and self.field2 is not None:
            raise ValidationError('Привычка не может иметь одновременно и связанную привычку, и вознаграждение.')
        elif self.field1 is None and self.field2 is None:
            raise ValidationError('У привычки не может не быть связанной привычки или вознаграждения.')
        return None


class RewardValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self):
