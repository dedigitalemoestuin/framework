from django.contrib.auth import views as auth_views


class LoginView(auth_views.LoginView):
    pass


class LogoutView(auth_views.LogoutView):
    pass


class PasswordChangeView(auth_views.PasswordChangeView):
    pass


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    pass


class PasswordResetView(auth_views.PasswordResetView):
    pass


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    pass


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    pass


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    pass
