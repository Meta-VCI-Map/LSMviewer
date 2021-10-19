
# risk_scores_calculation/urls.py

from django.urls import include, path
from rest_framework import routers
from risk_scores_calculation.views import RequestViewSet

router = routers.DefaultRouter()
router.register('calculate-risk-score', RequestViewSet, basename='lis'), #.calculate_risk_score()



urlpatterns = [

    path('', include(router.urls)),

]