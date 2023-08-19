import re

from django.core.exceptions import ValidationError


def validate_username(value):
    if not re.match(r'^[a-zA-Z0-9_]+$', value):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


def age_validate(value):
    if value <= 0:
        raise ValidationError('The age cannot be below 0.')
