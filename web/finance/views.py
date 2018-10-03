from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncMonth

from rest_framework import generics, viewsets
from .models import Income, Outcome, Reimbursement
from .serializers import IncomeSummarySerializer, OutcomeSerializer, ReimbursementSerializer

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

        if (from_date is not None and until_date is not None):
            queryset = queryset.filter(income_date_lte= until_date, income_date_gte= from_date).annotate(month = TruncMonth('income_date')).annotate(total_income = Count('income'))
        else :
            queryset = queryset.annotate(time = TruncMonth('income_date')).values('month').annotate(total_income = Count('income')).order_by('month')

        return queryset

class OutcomeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Outcome.objects.all()
    serializer_class = OutcomeSerializer

class ReimbursementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reimbursement.objects.all()
    serializer_class = ReimbursementSerializer