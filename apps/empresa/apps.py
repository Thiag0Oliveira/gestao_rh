from django.apps import AppConfig


class EmpresaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.empresa' #coloquei o app. antes do nome empresa porque não estava encontrando
