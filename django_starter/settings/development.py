from django_starter.settings.production import *

TMP_PATH = os.path.abspath(os.path.join(PROJECT_ROOT, 'tmp'))

DEBUG = TEMPLATE_DEBUG = True
SECRET = '42'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(TMP_PATH, 'db.sqlite3'),
    }
}

if DEBUG:
  # Local Statics Settings
  STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
  STATIC_URL = '/static/'
  MEDIA_URL = '/media/'

  STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')
  MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')

INTERNAL_IPS = ('127.0.0.1',)

if 'debug_toolbar' not in INSTALLED_APPS:
    INSTALLED_APPS += ('debug_toolbar',)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
