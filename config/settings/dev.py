"""Local development settings."""

from .base import *  # noqa: F403

DEBUG = True

# Convenient local access. Add test-server hostnames explicitly if needed.
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]

# Print emails to the terminal instead of sending real messages.
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Prevent accidental use of production-only cookie settings locally.
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
