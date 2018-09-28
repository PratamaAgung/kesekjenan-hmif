from django.contrib import admin

from .models import Income

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('income_date', 'description', 'income')
    search_fields = ('description', )
    list_filter = ('income_date', )

admin.site.register(Income, IncomeAdmin)
