from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ecom",
        "USER": "grizzly",
        "PASSWORD": "pandu",
        "HOST": "w3-django-project.cdxmgq9zqqlr.us-east-1.rds.amazonaws.com",
        "PORT": "5432",
    }
}
