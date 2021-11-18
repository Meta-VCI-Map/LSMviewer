# risk_scores_calculation/serializers.py

from .models import InfarctImage, CoefficientImage, RequestResult
from rest_framework.serializers import ModelSerializer

class InfarctImageSerializer(ModelSerializer):
    class Meta:
        model = InfarctImage
        fields = (
            'image'
                  )

class CoefficientImageSerializer(ModelSerializer):
    class Meta:
        model = CoefficientImage
        fields = (
            'image'
                  )

class CombinedSerializer(ModelSerializer):
    class Meta:
        model = RequestResult
        fields = (
            'infarct_image',
            'coefficient_image',
                  )
