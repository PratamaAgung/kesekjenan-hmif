from django.db import models
from datetime import date

class Income(models.Model):
    income_date = models.DateField(default= date.today)
    description = models.CharField(max_length = 100)
    income = models.DecimalField(max_digits= 10, decimal_places= 3)
