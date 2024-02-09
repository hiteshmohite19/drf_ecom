from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "drf_ecom",
        "USER": "grizzly",
        "PASSWORD": "pandu",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
