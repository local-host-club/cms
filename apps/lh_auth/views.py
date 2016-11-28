from django.urls import reverse_lazy
from django.views.generic import DetailView, RedirectView
from django.views.generic.edit import FormView
from allauth.account.views import LoginView, SignupView, LogoutView
from braces.views import LoginRequiredMixin
from apps.lh_auth.models import *
from apps.lh_auth.forms import *


class UserLogin(LoginView):
    template_name = 'lh_auth/login.html'


class UserSignUp(SignupView):
    template_name = 'lh_auth/sign_up.html'
    form_class = CustomSignupForm


class CustomLogoutView(LogoutView, FormView):
    form_class = CustomLogoutForm
    template_name = 'lh_auth/logout.html'
    success_url = reverse_lazy('custom_logout')


class CurrentPerfilDetail(LoginRequiredMixin, RedirectView):
    pattern_name = 'perfil_detail'

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('perfil_detail', kwargs={'pk': self.request.user.perfil.id})


class PerfilDetail(DetailView):
    template_name = 'lh_auth/perfil_detail.html'
    model = Perfil
