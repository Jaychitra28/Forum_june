from config.env import env

from .base import *

DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["127.0.0.1", "forumfix.com"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
