# risk_scores_calculation/forms.py

from django import forms
from .models import InfarctImage


class FileForm(forms.ModelForm):
    class Meta:
        model = InfarctImage
        fields = [
            'image',

        ]