import sys

if sys.argv[1:2] == ["test"]:
    PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # ruff: ignore[line-too-long]
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "accounts.CustomUser"
LOGIN_URL = "/auth/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/auth/login/"

AUTHENTICATION_BACKENDS = [
    "allauth.account.auth_backends.AuthenticationBackend",
]

# django-allauth

ACCOUNT_ADAPTER = "core.adapters.AccountAdapter"

ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_LOGIN_BY_CODE_REQUIRED = {"password", "mfa"}

ACCOUNT_USER_MODEL_USERNAME_FIELD = None

ACCOUNT_SIGNUP_ENABLED = False
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]

ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_UNKNOWN_ACCOUNTS = False
ACCOUNT_CHANGE_EMAIL = False
ACCOUNT_MAX_EMAIL_ADDRESSES = 1

ACCOUNT_EMAIL_SUBJECT_PREFIX = ""
