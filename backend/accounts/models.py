from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomerUserManager

class CustomUser(AbstractBaseUser):
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    email = models.EmailField(_("email"), unique=True)
    is_active = models.BooleanField(_("is active"), default=True)

    is_staff = models.BooleanField(_("is staff"), default=False)
    is_superuser = models.BooleanField(_("is superuser"), default=False)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomerUserManager()

    def get_full_name(self) -> str:
        return self.email

    def get_short_name(self) -> str:
        return self.email

    def __str__(self) -> str:
        return self.email