from django.db import models
from core.models import TimeStampedModel


class WishList(TimeStampedModel):

    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        "users.User", related_name="wishlist", on_delete=models.CASCADE
    )
    guesthouse = models.ForeignKey(
        "guesthouses.GuestHouse", related_name="wishlist", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Wish List"
