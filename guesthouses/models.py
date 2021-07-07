from django.db import models
from core.models import TimeStampedModel


class Photo(TimeStampedModel):
    caption = models.CharField(max_length=50)
    file = models.ImageField(upload_to="guesthouse_photos")
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
    photo = models.ImageField(blank=True, null=True, upload_to="signature_photo")
    price = models.IntegerField(default=0)
    start_at = models.TimeField(null=True)
    signature_type = models.ForeignKey(
        "SignatureType",
        related_name="Signature",
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        name= f"{self.signature_type} - {self.name}"
        return name


class GuestHouse(TimeStampedModel):

    """GuestHouse"""
    
    jeju="제주시"
    jochen="조천읍"
    gujwa="구좌읍"
    udo="우도"
    seongsan="성산읍"
    pyoseon="포선면"
    namwon="남원읍"
    seogwipo="서귀포시"
    jungmun="중문"
    andeok="안덕면"
    daejeong="대정읍"
    hankyung="한경읍"
    hanlim="한림읍"
    aewol="애월읍"

    CITY_CHOICE=(
    (jeju, "제주시"),
    (jochen, "조천읍"),
    (gujwa, "구좌읍"),
    (udo, "우도"),
    (seongsan, "성산읍"),
    (pyoseon, "포선면"),
    (namwon, "남원읍"),
    (seogwipo, "서귀포시"),
    (jungmun, "중문"),
    (andeok, "안덕면"),
    (daejeong, "대정읍"),
    (hankyung, "한경면"),
    (hanlim, "한림읍"),
    (aewol, "애월읍"),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    city = models.CharField(choices=CITY_CHOICE, max_length=80)
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
