from django.contrib import admin

from .models import StockRecord


class StockRecordAdmin(admin.ModelAdmin):
    list_display = ('day', 'closing_record')


admin.site.register(StockRecord, StockRecordAdmin)
