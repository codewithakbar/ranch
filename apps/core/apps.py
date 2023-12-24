from django.apps import AppConfig
from importlib import import_module


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'

    def ready(self) -> None:
        # Without this import, admin panel will not include this app
        import_module('apps.core.web.admin')
