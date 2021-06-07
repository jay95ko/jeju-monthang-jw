from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    MALE = "Male"
    FEMALE = "Female"
    GENDER_CHOICE = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )

    gender = models.CharField(choices=GENDER_CHOICE, max_length=10)
    age = models.IntegerField(default=0)
    avatar = models.ImageField(blank=True)
    birthdate = models.DateField(null=True)
    host = models.BooleanField(default=False)
