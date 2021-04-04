from django.apps import AppConfig


class SentimateConfig(AppConfig):
    name = 'SentiMate'

    def ready(self):
    	import SentiMate.signals