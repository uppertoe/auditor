from .base import *
from .secret_settings import dev_secret_key

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = dev_secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}