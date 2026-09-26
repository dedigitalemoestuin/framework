from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomerUserManager(BaseUserManager):
    def create_user(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)        

    
    def create_superuser(self, email: sr, password: str, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))

        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email: str, password: str, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))

        normalized_email = self.normalize_email(email)
        
        user = self.model(email=normalized_email, **extra_fields)
        user.set_password(password)
        user.save()

        return user