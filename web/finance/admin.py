from django.contrib import admin

from .models import Income

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('income_date', 'description', 'income')
    list_filter = ('income_date', 'description')

admin.site.register(Income, IncomeAdmin)
