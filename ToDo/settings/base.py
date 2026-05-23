import mimetypes
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

SECRET_KEY = 'django-insecure-z961-n60z2*-xzle^38zj1#-ld_vp*-)=nf_#o*!2r&u5imun5'
DEBUG = (os.getenv("DEBUG", "True") == "True")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")
mimetypes.add_type("application/javascript", ".js", True)
mimetypes.add_type("text/css", ".css", True)

INSTALLED_APPS = [

    # Django Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third Party Apps
    "django_htmx",
    "django_static_fontawesome",
    "django_ckeditor_5",

    # Local Apps
    "home",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # HTMX
    "django_htmx.middleware.HtmxMiddleware",
]

ROOT_URLCONF = "ToDo.urls"

WSGI_APPLICATION = "ToDo.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR , "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

AUTH_USER_MODEL = "home.CustomUser"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator"
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator"
    },
    {
        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = ("django.db.models.BigAutoField")
CKEDITOR_5_FILE_STORAGE = ("django.core.files.storage.FileSystemStorage")
CKEDITOR_5_UPLOAD_PATH = "uploads/"
CUSTOM_COLOR_PALETTE = [
    {
        "color": "hsl(4, 90%, 58%)",
        "label": "Red",
    },
    {
        "color": "hsl(340, 82%, 52%)",
        "label": "Pink",
    },
    {
        "color": "hsl(291, 64%, 42%)",
        "label": "Purple",
    },
]

CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "underline",
            "link",
            "|",
            "bulletedList",
            "numberedList",
            "|",
            "blockQuote",
            "codeBlock",
            "|",
            "undo",
            "redo",
        ],
    },
    "extends": {
        "blockToolbar": [
            "paragraph",
            "heading1",
            "heading2",
            "heading3",
            "|",
            "bulletedList",
            "numberedList",
            "|",
            "blockQuote",
        ],
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "underline",
            "strikethrough",
            "link",
            "|",
            "bulletedList",
            "numberedList",
            "todoList",
            "|",
            "outdent",
            "indent",
            "|",
            "insertImage",
            "insertTable",
            "mediaEmbed",
            "|",
            "blockQuote",
            "codeBlock",
            "|",
            "fontColor",
            "fontBackgroundColor",
            "|",
            "undo",
            "redo",
        ],
        "fontColor": {
            "colors": CUSTOM_COLOR_PALETTE,
        },
        "fontBackgroundColor": {
            "colors": CUSTOM_COLOR_PALETTE,
        },
        "table": {
            "contentToolbar": [
                "tableColumn",
                "tableRow",
                "mergeTableCells",
                "tableProperties",
                "tableCellProperties",
            ],
        },
    },
}

X_FRAME_OPTIONS = "SAMEORIGIN"
CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
