from django.db import models
from core.models import TimeStampedModel


class Photo(TimeStampedModel):
    caption = models.CharField(max_length=50)
    file = models.ImageField(upload_to="room_photos")
    guesthouse = models.ForeignKey(
        "GuestHouse", related_name="room_photos", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.caption


class SignatureType(TimeStampedModel):

    signature_type = models.CharField(max_length=50)

    def __str__(self):
        return self.signature_type


class Signature(TimeStampedModel):

    """GuestHouse Signature"""

    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(blank=True, null=True)
    price = models.IntegerField(default=0)
    start_at = models.TimeField(null=True)
    signature_type = models.ManyToManyField(
        "SignatureType",
        related_name="Signature",
        blank=True,
    )

    def __str__(self):
        return self.name


class GuestHouse(TimeStampedModel):

    """GuestHouse"""

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    address = models.CharField(max_length=200)
    check_in = models.TimeField()
    check_out = models.TimeField()
    signature = models.ManyToManyField(
        "Signature", related_name="GuestHouse", blank=True
    )

    host = models.ForeignKey(
        "users.User", related_name="guesthouse", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Guest House"

    def __str__(self):
        return self.name
