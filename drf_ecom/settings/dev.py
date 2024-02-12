from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ecom_drf",
        "USER": "grizzly",
        "PASSWORD": "pandu",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
