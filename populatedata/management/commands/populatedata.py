from django.core.management.base import BaseCommand
from populatedata.factories import UserFactory, ActivityPeriodFactory


# create custom management command to populate dummy data of user and its activities
class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for entry in range(total):
            UserFactory.create()
            ActivityPeriodFactory.create()

        self.stdout.write("Database populated successfully with dummy data")



