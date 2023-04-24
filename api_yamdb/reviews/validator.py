import datetime as dt

from django.core.exceptions import ValidationError


def year_validate(value):
    current_year = dt.date.today().year
    if value > current_year:
        raise ValidationError(
            'Проверьте год выпуска. Не может быть больше текущего'
        )
    return value
