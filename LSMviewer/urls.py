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
#from risk_scores_calculation.views import filefield_upload
from importlib import import_module
from .common import LSMviewerCommonSettings, riskScoreAppViews, riskScoreAppUrls

settings = import_module(LSMviewerCommonSettings)
app_views = import_module(riskScoreAppViews)
app_urls = import_module(riskScoreAppViews)

urlpatterns = [
    path('', app_views.filefield_upload, name="upload"),

    # API endpoints
    path('', include(riskScoreAppUrls)), #'risk_scores_calculation.urls'

# When running in production, edit the path as following:
# path('', include('LSMviewer.risk_scores_calculation.urls')),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
