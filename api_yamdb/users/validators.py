from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class NotEqualValidator(BaseValidator):

    def compare(self, a, b):
        return a == b.lower()
