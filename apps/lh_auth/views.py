from django.views.generic import DetailView
from apps.lh_auth.models import *
from apps.lh_auth.forms import *
from allauth.account.views import LoginView, SignupView


class UserLogin(LoginView):
    template_name = 'lh_auth/login.html'


class UserSignUp(SignupView):
    template_name = 'lh_auth/sign_up.html'
    form_class = CustomSignupForm


class PerfilDetail(DetailView):
    template_name = 'lh_auth/perfil_detail.html'
    model = Perfil
