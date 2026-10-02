from django.db import models
from urlsandviewsexercise.models import TimestampMixin


class Review(TimestampMixin):
    author = models.CharField(
        max_length=100,
    )
    body = models.TextField()
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )
    is_published = models.BooleanField(
        default=True,
    )
    destination = models.ForeignKey(
        to='destinations.Destination',
        on_delete=models.CASCADE,
        related_name="reviews"
    )
