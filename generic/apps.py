from django.apps import AppConfig


class GenericConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'generic'

    def ready(self) -> None:
        from generic import signals
        return super().ready()
