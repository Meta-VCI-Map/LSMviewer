from django.apps import AppConfig
from LSMviewer.common import *

class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = BASE_PATH + 'risk_scores_calculation'
    #name = 'risk_scores_calculation'