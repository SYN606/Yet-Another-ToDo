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

# Extra locations for static files (development only)
STATICFILES_DIRS = [
    BASE_DIR / "home/static",  # Any static folder in your apps
]

TAILWIND_APP_NAME = "theme"

INTERNAL_IPS = [
    "127.0.0.1",
]
