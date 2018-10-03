from django.conf.urls import url, include
from rest_framework import routers
from .views import IncomeViewSet, OutcomeViewSet, ReimbursementViewSet, IncomeSummaryViewSet, OutcomeSummaryViewSet, ReimbursementSummaryViewSet

router = routers.DefaultRouter()
router.register(r'income', IncomeViewSet)
router.register(r'outcome', OutcomeViewSet)
router.register(r'reimbursement', ReimbursementViewSet)

urlpatterns = [
    url(r'^income-summary/$', IncomeSummaryViewSet.as_view(), name = 'income-summary-list'),
    url(r'^outcome-summary/$', OutcomeSummaryViewSet.as_view(), name = 'outcome-summary-list'),
    url(r'^reimbursement-summary/$', ReimbursementSummaryViewSet.as_view(), name = 'reimbursement-summary-list'),
    url(r'^', include(router.urls)),
]