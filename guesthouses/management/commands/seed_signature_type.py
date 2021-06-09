import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users.models import User
from guesthouses.models import GuestHouse, Signature, SignatureType


class Command(BaseCommand):

    help = "This command creates many SignatureType"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many SignatureType you want to create",
        )

    def handle(self, *args, **options):
        Signature_Type = [
            "Party",
            "SnapShot",
            "Camping",
            "Drunken",
            "Night Tour",
            "Morning Tour",
            "Good Meal",
            "Swimming",
            "Wine",
        ]
        for a in Signature_Type:
            SignatureType.objects.create(signature_type=a)
        self.stdout.write(self.style.SUCCESS("SignatureType created!"))
