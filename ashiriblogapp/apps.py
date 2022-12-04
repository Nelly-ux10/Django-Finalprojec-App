from django.apps import AppConfig


class AshiriblogappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ashiriblogapp'



def ready(self):
		import ashiriblogapp.signals