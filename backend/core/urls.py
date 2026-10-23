"""URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from django.urls import include, path
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView
from rest_framework.routers import DefaultRouter

from accounts.views import UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path(
        "auth/email/", RedirectView.as_view(pattern_name="mfa_index", permanent=False)
    ),
    path(
        "auth/signup/",
        RedirectView.as_view(pattern_name="account_login", permanent=False),
    ),
    path("auth/", include("allauth.urls")),
    path("api/", include(router.urls)),
    path("", TemplateView.as_view(template_name="core/index.html"), name="index"),
]
