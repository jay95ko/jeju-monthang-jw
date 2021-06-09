import random
from django.core.management.base import BaseCommand, LabelCommand
from django_seed import Seed
from reviews.models import Review
from guesthouses.models import GuestHouse
from users.models import User


class Command(BaseCommand):

    help = "This command creates many reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many reviews you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        guesthouse = GuestHouse.objects.all()
        user = User.objects.all()
        seeder.add_entity(
            Review,
            number,
            {
                "guesthouse": lambda x: random.choice(guesthouse),
                "rating": lambda x: random.randint(1, 5),
                "user": lambda x: random.choice(user),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))
