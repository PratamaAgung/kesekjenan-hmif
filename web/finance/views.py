from django.shortcuts import render

from rest_framework import viewsets
from .models import Income, Outcome, Reimbursement
from .serializers import IncomeSerializer, OutcomeSerializer, ReimbursementSerializer

class IncomeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = IncomeSerializer

    list_for_each = request.query_params.get('each')
    from_date = request.query_params.get('from')
    until_date = request.query_params.get('until')

    if (list_for_each is None):
        list_for_each = 'day'

    if (from_date is not None and until_date is not None):
        queryset = Income.objects.filter(income_date_lte= until_date, income_date_gte= from_date).values_list(list_for_each).annotate(total_income = Count('income'))
    else :
        queryset = Income.objects.all().values_list(list_for_each).annotate(total_income = Count('income'))

class OutcomeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Outcome.objects.all()
    serializer_class = OutcomeSerializer

class ReimbursementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reimbursement.objects.all()
    serializer_class = ReimbursementSerializer