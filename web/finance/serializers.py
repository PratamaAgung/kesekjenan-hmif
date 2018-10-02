from rest_framework import serializers
from .models import Income, Outcome, Reimbursement

class IncomeSerializer(serializers.ModelSerializer):
    month = serializers.DateField()
    total_income = serializers.DecimalField()
    
    class Meta:
        model = Income
        fields = '__all__'

class OutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outcome
        fields = '__all__'

class ReimbursementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reimbursement
        fields = '__all__'
