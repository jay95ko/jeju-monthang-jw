import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users.models import User
from guesthouses.models import GuestHouse, Signature, SignatureType


class Command(BaseCommand):

    help = "This command creates many Signature"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many Signature you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        Signature_Type = SignatureType.objects.all()
        seeder.add_entity(
            Signature,
            number,
            {
                "name": lambda x: seeder.faker.name(),
                "price": lambda x: random.randint(10000, 50000),
                "signature_type": lambda x: random.choice(Signature_Type),
            },
        )
        create_something = seeder.execute()
        

        self.stdout.write(self.style.SUCCESS(f"{number} Signature created!"))
