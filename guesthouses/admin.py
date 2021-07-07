from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Signature)
class SignatureAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "signature_type",
        "price",
        "start_at",
    )
    list_filter = ("signature_type",)

    search_fields = ("signature_type",)


@admin.register(models.SignatureType)
class SignatureTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.GuestHouse)
class GuestHouseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "city",
        "price",
        "address",
        "host",
        "check_in",
        "check_out",
    )
    list_filter = (
        "signature",
        "city",
        "price",
    )
