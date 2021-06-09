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
            },
        )
        create_something = seeder.execute()
        create_clean = flatten(list(create_something.values()))
        for pk in create_clean:
            signature = Signature.objects.get(pk=pk)
            a = random.choice(Signature_Type)
            signature.signature_type.add(a)

        self.stdout.write(self.style.SUCCESS(f"{number} Signature created!"))
