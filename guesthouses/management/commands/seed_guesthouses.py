import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users.models import User
from guesthouses.models import GuestHouse, Signature, Photo
from guesthouses import models as guesthouse_models


class Command(BaseCommand):

    help = "This command creates many GuestHouses"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many GuestHouses you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_host = User.objects.filter(host=True)
        seeder.add_entity(
            GuestHouse,
            number,
            {
                "name": lambda x: seeder.faker.name() + "'s GusetHouse",
                "price": lambda x: random.randint(10000, 50000),
                "host": lambda x: random.choice(all_host),
            },
        )
        create_something = seeder.execute()
        create_clean = flatten(list(create_something.values()))
        signature = Signature.objects.all()
        for pk in create_clean:
            guesthouse = GuestHouse.objects.get(pk=pk)
            for a in signature:
                random_number = random.randint(0, 10)
                if random_number % 2 == 0:
                    guesthouse.signature.add(a)
            for i in range(2, random.randint(5, 10)):
                Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    guesthouse=guesthouse,
                    file=f"guesthouse_photos/{random.randint(1, 31)}.webp",
                )
        self.stdout.write(self.style.SUCCESS(f"{number} GuestHouses created!"))
