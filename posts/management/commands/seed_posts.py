import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from posts import models as post_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command makes many posts."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many posts you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        writer = user_models.User.objects.filter(pk=2)
        categories = post_models.Category.objects.all()
        seeder.add_entity(
            post_models.Post,
            number,
            {
                "category": lambda x: random.choice(categories),
                "title": lambda x: seeder.faker.address(),
                "writer": lambda x: random.choice(writer),
                "body": lambda x: seeder.faker.text(),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Posts created!"))
