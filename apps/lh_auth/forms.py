from allauth.account.forms import SignupForm
from django import forms
from apps.lh_auth.models import *


class CustomLogoutForm(forms.Form):
    perfil = forms.CharField(required=False, widget=forms.HiddenInput())


class CustomSignupForm(SignupForm):
    GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('S', 'Sin especificar'),)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    genero = forms.ChoiceField(choices=GENERO_CHOICES)
    fecha_nacimiento = forms.DateField(required=False)
    direccion = forms.CharField(required=False)

    class Meta:
        model = Perfil

    def save(self, commit=True, *args, **kwargs):
        user = super(CustomSignupForm, self).save(commit)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.perfil.genero = self.cleaned_data['genero']
        user.perfil.fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        user.perfil.direccion = self.cleaned_data['direccion']
        user.save()
        user.perfil.save()
        return user
