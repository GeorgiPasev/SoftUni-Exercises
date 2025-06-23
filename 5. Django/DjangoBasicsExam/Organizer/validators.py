import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class AlphaNumericHyphenSpaceValidator:
    message = "The company name is invalid!"
    code = "invalid"
    regex = r'^[A-Za-z0-9\s-]+$'

    def __init__(self, message=None, code=None):
        if message:
            self.message = message
        if code:
            self.code = code

    def __call__(self, value):
        if not re.fullmatch(self.regex, value):
            raise ValidationError(self.message, code=self.code)


def phone_validator(value):
    if not value.isdigit():
        raise ValidationError("Phone number must contain digits only.")
    if len(value) > 15:
        raise ValidationError("Phone number must be 15 digits maximum.")


@deconstructible
class SecretKeyValidator:
    message = "Your secret key must have 4 unique digits!"
    code = "invalid"

    def __call__(self, value):
        if len(value) != 4 or not value.isdigit() or len(set(value)) != 4:
            raise ValidationError(self.message, code=self.code)