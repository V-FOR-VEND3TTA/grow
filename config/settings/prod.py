"""Production settings for Render."""

from .base import *  # noqa: F403
from .base import env

DEBUG = False

# Required production secret. Never use a development fallback here.
SECRET_KEY = env("SECRET_KEY")

# Configure these explicitly in the Render environment.
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])

# PostgreSQL connection supplied by Render.
DATABASES = {
    "default": env.db("DATABASE_URL"),
}

DATABASES["default"]["CONN_MAX_AGE"] = 600
DATABASES["default"]["CONN_HEALTH_CHECKS"] = True

# Set DB_SSL_REQUIRE=False only if the chosen database connection
# explicitly does not support or require SSL.
DATABASES["default"]["OPTIONS"] = {
    **DATABASES["default"].get("OPTIONS", {}),
    "sslmode": (
        "require"
        if env.bool("DB_SSL_REQUIRE", default=True)
        else "prefer"
    ),
}

# HTTPS and secure cookies.
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

# Render terminates HTTPS at its proxy. Trust forwarded HTTPS only
# when the application is deployed behind that trusted proxy.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# HSTS: enable after verifying HTTPS works correctly on the production
# domain. Start conservatively; increase the duration after validation.
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

# Production email: configure SMTP credentials through environment
# variables when an email provider has been selected.
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="")
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
EMAIL_USE_SSL = env.bool("EMAIL_USE_SSL", default=False)
