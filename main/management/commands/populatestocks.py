import datetime
import random

from django.core.management.base import BaseCommand, CommandError

from main.models import StockRecord


class Command(BaseCommand):
    help = "Save randomly generated stock record values."

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument(
            'number_of_stock_records',
            type=int,
            help="Number of stock records to generate and save to database"
        )

        # Named (optional) arguments
        parser.add_argument(
            '--delete-existing',
            action='store_true',
            dest='delete_existing',
            default=False,
            help='Delete existing stock records before generating new ones',
        )

    def get_date(self):
        # Naively generating a random date
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(2014, 2017)
        return datetime.date(year, month, day)

    def handle(self, *args, **options):
        records = []
        size = options["number_of_stock_records"]
        if size < 0 or size > 10000:
            raise CommandError("You can only generate 1-10000 stock records at a go")
        for _ in range(size):
            kwargs = {
                'day': self.get_date(),
                'closing_record': random.randint(1, 1000)
            }
            record = StockRecord(**kwargs)
            records.append(record)
        if options["delete_existing"]:
            StockRecord.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Existing stock records deleted.'))
        StockRecord.objects.bulk_create(records)
        self.stdout.write(self.style.SUCCESS('{} Stock records saved.'.format(size)))
