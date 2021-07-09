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
        "email_verified",
        "email_secret",
        "login_method",
    )

    list_filter = (
        "gender",
        "age",
        "host",
        
    )

    search_fields = ("username",)

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
                    "login_method",
                )
            },
        ),
    )
