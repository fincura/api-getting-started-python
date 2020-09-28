import os
from jinja2.environment import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings

class JinjaEnvironment(Environment):
    def __init__(self,**kwargs):
        super(JinjaEnvironment, self).__init__(**kwargs)
        self.globals['app_label'] = settings.APP_LABEL