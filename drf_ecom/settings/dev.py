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
CORS_ORIGIN_ALLOW_ALL = False
ALLOWED_HOSTS = ["localhost", "localhost:3000", "127.0.0.1:3000"]
CORS_ORIGIN_WHITELIST = (
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
)
