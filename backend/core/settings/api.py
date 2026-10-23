REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # TokenAuthentication is allowed (and even encouraged) but should be set per API
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        # No access by default. Each endpoint needs to define its own access rules
        "core.permissions.AllowNone",
    ],
}
