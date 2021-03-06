from django.apps import AppConfig

prod_mode = False
if prod_mode:
    from LSMviewer.LSMviewer.common import *
else:
    from LSMviewer.common import *

class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = BASE_PATH + 'risk_scores_calculation'