from django.db import models
from core.models import TimeStampedModel


class Review(TimeStampedModel):

    guesthouse = models.ForeignKey(
        "guesthouses.GuestHouse", related_name="reviews", on_delete=models.CASCADE
    )
    Advantage_review = models.TextField(null=True)
    Weakness_review = models.TextField(null=True)
    rating = models.IntegerField(default=5)

    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.guesthouse} - {self.rating}"
