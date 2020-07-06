from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!gw-10ywlgueh5^m%b%5*nitfh=f2$hzm$rqq6q7j570fi!i9r'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# 172.17.0.1 is Docker private network
INTERNAL_IPS = ('127.0.0.1', '172.17.0.1')


try:
    from .local import *
except ImportError:
    pass
