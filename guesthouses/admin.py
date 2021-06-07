from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Signature)
class SignatureAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "start_at",
    )
    list_filter = ("signature_type",)


@admin.register(models.SignatureType)
class SignatureTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.GuestHouse)
class GuestHouseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "address",
        "check_in",
        "check_out",
    )
    list_filter = (
        "signature",
        "price",
    )
