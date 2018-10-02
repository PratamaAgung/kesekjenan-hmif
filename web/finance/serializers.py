from rest_framework import serializers
from .models import Income, Outcome, Reimbursement

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ('income_date', 'income')
class OutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outcome
        fields = '__all__'

class ReimbursementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reimbursement
        fields = '__all__'
