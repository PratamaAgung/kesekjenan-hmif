from django.shortcuts import render

from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncDay

from rest_framework import generics, viewsets
from .models import Income, Outcome, Reimbursement
from .serializers import IncomeSerializer, OutcomeSerializer, ReimbursementSerializer, IncomeSummarySerializer, OutcomeSummarySerializer, ReimbursementSummarySerializer

class IncomeSummaryViewSet(generics.ListAPIView):
    serializer_class = IncomeSummarySerializer
    queryset = Income.objects.all()

    def get_queryset(self):
        list_for_each = self.request.query_params.get('each')
        from_date = self.request.query_params.get('from')
        until_date = self.request.query_params.get('until')
        queryset = Income.objects

        if (list_for_each is None):
            list_for_each = 'day'

        if (list_for_each == 'day'):
            trunc = TruncDay('income_date')
        else:
            trunc = TruncMonth('income_date')

        if (from_date is not None and until_date is not None):
            queryset = queryset.filter(income_date__range=[from_date, until_date]).annotate(time = trunc).values('time').annotate(total_income = Sum('income')).order_by('time')
        else :
            queryset = queryset.annotate(time = trunc).values('time').annotate(total_income = Sum('income')).order_by('time')

        return queryset

class OutcomeSummaryViewSet(generics.ListAPIView):
    serializer_class = OutcomeSummarySerializer
    queryset = Outcome.objects.all()

    def get_queryset(self):
        list_for_each = self.request.query_params.get('each')
        from_date = self.request.query_params.get('from')
        until_date = self.request.query_params.get('until')
        queryset = Outcome.objects

        if (list_for_each is None):
            list_for_each = 'day'

        if (list_for_each == 'day'):
            trunc = TruncDay('outcome_date')
        else:
            trunc = TruncMonth('outcome_date')

        if (from_date is not None and until_date is not None):
            queryset = queryset.filter(outcome_date__range=[from_date, until_date]).annotate(time = trunc).values('time').annotate(total_outcome = Sum('outcome')).order_by('time')
        else :
            queryset = queryset.annotate(time = trunc).values('time').annotate(total_outcome = Sum('outcome')).order_by('time')

        return queryset

class ReimbursementSummaryViewSet(generics.ListAPIView):
    serializer_class = ReimbursementSummarySerializer
    queryset = Reimbursement.objects.all()

    def get_queryset(self):
        list_for_each = self.request.query_params.get('each')
        from_date = self.request.query_params.get('from')
        until_date = self.request.query_params.get('until')
        queryset = Reimbursement.objects

        if (list_for_each is None):
            list_for_each = 'day'

        if (list_for_each == 'day'):
            trunc = TruncDay('reimbursement_date')
        else:
            trunc = TruncMonth('reimbursement_date')

        if (from_date is not None and until_date is not None):
            queryset = queryset.filter(reimbursement_date__range=[from_date, until_date]).annotate(time = trunc).values('time').annotate(total_reimbursement = Sum('reimbursement')).order_by('time')
        else :
            queryset = queryset.annotate(time = trunc).values('time').annotate(total_reimbursement = Sum('reimbursement')).order_by('time')

        return queryset

class IncomeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class OutcomeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Outcome.objects.all()
    serializer_class = OutcomeSerializer

class ReimbursementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reimbursement.objects.all()
    serializer_class = ReimbursementSerializer