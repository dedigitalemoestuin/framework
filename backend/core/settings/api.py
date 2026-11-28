REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # BasicAuthentication is removed on purpose.
        # Docs describe it as "only appropriate for testing"
        # TokenAuthentication is allowed (and even encouraged) but should be set per API
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        # No access by default. Each endpoint needs to define its own access rules
        "core.permissions.AllowNone",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Framework API",
    "DESCRIPTION": "Framework API",
    "VERSION": "0.0.1",
    "SERVE_INCLUDE_SCHEMA": False,
    "SERVE_PERMISSIONS": ["core.permissions.AllowNone"],
}
