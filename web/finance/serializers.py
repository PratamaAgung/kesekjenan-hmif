from rest_framework import serializers
from .models import Income, Outcome, Reimbursement

class IncomeSummarySerializer(serializers.ModelSerializer):
    time = serializers.DateField()
    total_income = serializers.DecimalField(max_digits= 10, decimal_places= 2)

    class Meta:
        model = Income
        fields = ('time', 'total_income')

class OutcomeSummarySerializer(serializers.ModelSerializer):
    time = serializers.DateField()
    total_income = serializers.DecimalField(max_digits= 10, decimal_places= 2)

    class Meta:
        model = Outcome
        fields = ('time', 'total_income')

class ReimbursementSummarySerializer(serializers.ModelSerializer):
    time = serializers.DateField()
    total_income = serializers.DecimalField(max_digits= 10, decimal_places= 2)

    class Meta:
        model = Reimbursement
        fields = ('time', 'total_income')

class IncomeSerializer(serializers.ModelSerializer):
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
