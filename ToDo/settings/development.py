from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True

# MIDDLEWARE += [
#     "django_browser_reload.middleware.BrowserReloadMiddleware",
# ]

ALLOWED_HOSTS = []

STATICFILES_DIRS = [
    BASE_DIR / "home/static", 
]

INTERNAL_IPS = [
    "127.0.0.1",
]
