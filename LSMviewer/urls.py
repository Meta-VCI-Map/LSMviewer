"""LSMviewer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from risk_scores_calculation.views import filefield_upload, RequestResultViewSet

urlpatterns = [
    path('risk-scores/', filefield_upload, name="upload"),

    # API endpoint
    path('calculate-location-risk-score', RequestResultViewSet.calculate_location_score, name="lis_calculation"),
    path('calculate-network-risk-score', RequestResultViewSet.calculate_network_score, name="nis_calculation"),
    path('download-network-risk-score', RequestResultViewSet.download_network_score, name="download_file"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)