from pathlib import Path
from django.conf import settings

from ranch import env


# Application definition
INSTALLED_APPS: list[str] = [
    "apps.core",
    "apps.users",
    "apps.home",
    "apps.news",
    "apps.gallery",
]

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", cast=bool, default=False)

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
LANGUAGE_CODE = env("LANGUAGE_CODE", cast=str, default="en-us")

TIME_ZONE = env("TIME_ZONE", cast=str, default="UTC")

USE_I18N = env("USE_I18N", cast=bool, default=True)

USE_TZ = env("USE_TZ", cast=bool, default=True)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


LANGUAGES = (
    ('en', 'English'),
    ('uz', 'O\'zbek'),
    ('ru', 'Русский'),
)

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_LANGUAGES = ('uz', 'en', 'ru')



LANGUAGE_SESSION_KEY = 'session_language_appname'
LANGUAGE_COOKIE_NAME = 'cookie_language_appname' 


# Rich Text Filed

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 700,
    },
}