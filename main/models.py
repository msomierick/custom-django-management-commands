from django.db import models


# Create your models here.
class StockRecord(models.Model):
    day = models.DateField()
    closing_record = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{}'.format(self.closing_record)
