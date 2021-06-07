from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "gender",
        "age",
        "host",
    )

    list_filter = (
        "gender",
        "age",
        "host",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "gender",
                    "age",
                    "avatar",
                    "birthdate",
                    "host",
                )
            },
        ),
    )
