from django.db import models
from datetime import date

class Income(models.Model):
    income_date = models.DateField(default= date.today)
    income_description = models.CharField(max_length = 256)
    income = models.DecimalField(max_digits= 10, decimal_places= 2)

    def __str__(self):
        return self.income_description

class Outcome(models.Model):
    outcome_date = models.DateField(default= date.today)
    outcome_description = models.CharField(max_length = 256)
    outcome = models.DecimalField(max_digits= 10, decimal_places= 2)

    def __str__(self):
        return self.outcome_description

class Reimbursement(models.Model):
    outcome_reference = models.ForeignKey(Outcome, on_delete= models.CASCADE)
    reimbursement_date = models.DateField(default= date.today)
    reimbursement_source = models.CharField(max_length = 256)
    reimbursement = models.DecimalField(max_digits= 10, decimal_places= 2)

    def __str__(self):
        return str(self.reimbursement_date) + "-" + self.reimbursement_source + "-" + str(self.outcome_reference)
