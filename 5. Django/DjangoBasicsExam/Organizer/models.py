from django.core.validators import MinLengthValidator
from django.db import models

from Organizer.validators import AlphaNumericHyphenSpaceValidator, phone_validator, SecretKeyValidator


class Organizer(models.Model):
    company_name = models.CharField(
        max_length=110,
        unique=True,
        validators=[
            MinLengthValidator(2),
            AlphaNumericHyphenSpaceValidator(),
        ],
        help_text="*Allowed names contain letters, digits, spaces, and hyphens."
    )

    phone_number = models.CharField(
        unique=True,
        max_length=15,
        validators=[phone_validator]
    )

    secret_key = models.CharField(
        max_length=4,
        validators=[SecretKeyValidator()],
        help_text="*Pick a combination of 4 unique digits."
    )

    website = models.URLField(
        null=True,
        blank=True,
    )