from django.contrib import admin
from .models import Income, Outcome
from rangefilter.filter import DateRangeFilter

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('income_date', 'income_description', 'income')
    search_fields = ('income_description', )
    list_filter = (('income_date', DateRangeFilter), )

class OutcomeAdmin(admin.ModelAdmin):
    list_display = ('outcome_date', 'outcome_description', 'outcome')
    search_fields = ('outcome_description', )
    list_filter = (('outcome_date', DateRangeFilter), )

admin.site.register(Income, IncomeAdmin)
admin.site.register(Outcome, OutcomeAdmin)