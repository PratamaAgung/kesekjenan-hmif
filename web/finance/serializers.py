from rest_framework import serializers
from .models import Income, Outcome, Reimbursement

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income

class OutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outcome

class ReimbursementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reimbursement