from django.conf.urls import url, include
from rest_framework import routers
from .views import IncomeSummaryViewSet, OutcomeViewSet, ReimbursementViewSet, api_root

router = routers.DefaultRouter()
router.register(r'outcome', OutcomeViewSet)
router.register(r'reimbursement', ReimbursementViewSet)

urlpatterns = [
    url(r'^income-summary/$', IncomeSummaryViewSet.as_view(), name = 'income-summary-list'),
    url(r'^', include(router.urls)),
    url(r'', include(api_root))
]