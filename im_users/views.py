from django.contrib.auth.views import LoginView


class ImUserLogin(LoginView):
    template_name = "im_users/login.html"
