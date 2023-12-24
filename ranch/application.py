from pathlib import Path
from django.conf import settings

from ranch import env


# Application definition
INSTALLED_APPS: list[str] = [
    "apps.core"
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
