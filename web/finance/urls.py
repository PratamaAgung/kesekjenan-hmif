from django.conf.urls import url, include
from rest_framework import routers
from .views import IncomeSummaryViewSet, OutcomeViewSet, ReimbursementViewSet

router = routers.DefaultRouter()
router.register(r'outcome', OutcomeViewSet)
router.register(r'reimbursement', ReimbursementViewSet)

urlpatterns = [
    url(r'^income-summary/$', IncomeSummaryViewSet.as_view(), name = 'income-list'),
    url(r'^', include(router.urls)),
]