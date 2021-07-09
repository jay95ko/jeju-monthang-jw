import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.aggregates import Max
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string


# Create your models here.


class User(AbstractUser):

    MALE = "Male"
    FEMALE = "Female"
    GENDER_CHOICE = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )

    LOGIN_EMAIL = "email"
    LOGING_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGING_KAKAO, "Kakao"),
    )

    gender = models.CharField(choices=GENDER_CHOICE, max_length=10)
    age = models.PositiveIntegerField(null=True)
    avatar = models.ImageField(blank=True, upload_to="avatars")
    birthdate = models.DateField(null=True)
    host = models.BooleanField(default=False)

    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default="", blank=True)

    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                "Verify JejuMonthang Account",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return
