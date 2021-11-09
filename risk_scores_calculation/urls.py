
# risk_scores_calculation/urls.py

from django.urls import include, path
from rest_framework import routers
from risk_scores_calculation.views import RequestResultViewSet

router = routers.DefaultRouter()
#router.register('calculate-risk-score', RequestViewSet, basename='lis'), #.calculate_risk_score()

urlpatterns = [
    #path('', include(router.urls)),

    # API endpoints
    path('calculate-location-risk-score', RequestResultViewSet.calculate_location_score, name="lis_calculation"),
    path('calculate-network-risk-score', RequestResultViewSet.calculate_network_score, name="nis_calculation"),
    path('download-network-risk-score', RequestResultViewSet.download_network_score, name="download_file"),
]