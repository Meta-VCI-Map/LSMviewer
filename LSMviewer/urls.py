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

try:
    '''Development'''
    from risk_scores_calculation.views import filefield_upload
    urlpatterns = [
        path('', filefield_upload, name="upload"),

        # API endpoints
        path('', include('risk_scores_calculation.urls')),
    ]

except:
    '''Deployment'''
    from LSMviewer.risk_scores_calculation.views import filefield_upload

    urlpatterns = [
        path('', filefield_upload, name="upload"),

        # API endpoints
        path('', include('LSMviewer.risk_scores_calculation.urls')),
    ]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
