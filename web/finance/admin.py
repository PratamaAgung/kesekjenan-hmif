from django.contrib import admin
from .models import Income
from rangefilter.filter import DateRangeFilter

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('income_date', 'description', 'income')
    search_fields = ('description', )
    list_filter = (('income_date', DateRangeFilter), )

admin.site.register(Income, IncomeAdmin)
