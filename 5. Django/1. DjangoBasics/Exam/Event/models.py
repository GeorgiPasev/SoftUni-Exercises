from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from Organizer.models import Organizer


class Event(models.Model):
    slogan = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
    )

    location = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
    )

    start_time = models.DateTimeField(
        default=timezone.now,
    )

    available_tickets = models.IntegerField(
        validators=[MinValueValidator(0)],
    )

    key_features = models.TextField(
        null=True,
        blank=True,
    )

    banner_url = models.URLField(
        null=True,
        blank=True,
    )

    organizer = models.ForeignKey(
        Organizer,
        on_delete=models.CASCADE,
        editable=False,
    )