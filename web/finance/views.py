from django.shortcuts import render

from rest_framework import viewsets
from .models import Income, Outcome, Reimbursement
from .serializers import IncomeSerializer, OutcomeSerializer, ReimbursementSerializer

class IncomeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class OutcomeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Outcome.objects.all()
    serializer_class = OutcomeSerializer

class ReimbursementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reimbursement.objects.all()
    serializer_class = ReimbursementSerializer