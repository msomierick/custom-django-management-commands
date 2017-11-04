from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase
from django.utils import timezone

from .models import StockRecord


def create_records():
    day = timezone.now()
    record2 = StockRecord(day=day, closing_record=10)
    record3 = StockRecord(day=day, closing_record=20)
    record1 = StockRecord(day=day, closing_record=30)
    StockRecord.objects.bulk_create([record1, record2, record3])


class PopulateStocksTestCase(TestCase):
    '''Tests for the populatestocks management command'''

    def test_positional_args_required(self):
        # Test that the command cannot be called without the number_of_stock_records
        msg = 'Error: the following arguments are required: number_of_stock_records'
        with self.assertRaisesMessage(CommandError, msg):
            call_command('populatestocks')

    def test_input_validation(self):
        # Test validation of number_of_stock_records positional argument
        msg = 'You can only generate 1-10000 stock records at a go'
        with self.assertRaisesMessage(CommandError, msg):
            call_command('populatestocks', -4)

        with self.assertRaisesMessage(CommandError, msg):
            call_command('populatestocks', 1000000)

    def test_records_saved(self):
        call_command('populatestocks', 10)

        self.assertEqual(StockRecord.objects.count(), 10)

    def test_existing_records_not_deleted_before_save(self):
        create_records()

        self.assertEqual(StockRecord.objects.count(), 3)

        call_command('populatestocks', 10)

        self.assertEqual(StockRecord.objects.count(), 13)

    def test_existing_records_deleted_before_save(self):
        create_records()

        self.assertEqual(StockRecord.objects.count(), 3)

        call_command('populatestocks', 10, delete_existing=True)

        self.assertEqual(StockRecord.objects.count(), 10)
