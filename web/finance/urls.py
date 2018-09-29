from django.conf.urls import url
from rest_framework import routers
from .views import IncomeViewSet, OutcomeViewSet, ReimbursementViewSet

router = routers.DefaultRouter()
router.register(r'income', IncomeViewSet)
router.register(r'outcome', OutcomeViewSet)
router.register(r'reimbursement', ReimbursementViewSet)

urlpatterns = router.urls