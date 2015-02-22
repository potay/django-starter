import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "django_starter.settings.development")

from django.core.wsgi import get_wsgi_application
from django_starter.settings.production import HEROKU

if HEROKU:
  from dj_static import Cling
  application = Cling(get_wsgi_application())
else:
  application = get_wsgi_application()

