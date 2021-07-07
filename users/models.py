from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.aggregates import Max

# Create your models here.


class User(AbstractUser):

    MALE = "Male"
    FEMALE = "Female"
    GENDER_CHOICE = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )

    gender = models.CharField(choices=GENDER_CHOICE, max_length=10)
    age = models.PositiveIntegerField(null=True)
    avatar = models.ImageField(blank=True, upload_to="avatars")
    birthdate = models.DateField(null=True)
    host = models.BooleanField(default=False)
