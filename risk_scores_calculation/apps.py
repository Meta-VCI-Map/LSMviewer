from django.apps import AppConfig

try:
    from LSMviewer.deployment_settings import DEBUG
except:
    from LSMviewer.settings import DEBUG

if DEBUG == True:
    '''Development'''
    class PagesConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'risk_scores_calculation'
else:
    class PagesConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'LSMviewer.risk_scores_calculation'