from django import forms
from django.forms import formset_factory
from django.forms.models import modelformset_factory
from apps.edu.models import *


class CompetenciaAreaForm(forms.ModelForm):
    class Meta:
        model = CompetenciaArea
        fields = '__all__'


class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = '__all__'


class IndicadorForm(forms.ModelForm):
    class Meta:
        model = Indicador
        fields = '__all__'


class IndicadorNivelForm(forms.ModelForm):
    class Meta:
        model = Indicador
        fields = ('id',)


class NivelForm(forms.ModelForm):
    class Meta:
        model = Nivel
        fields = '__all__'


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ('descripcion',)


NotaFormSet = modelformset_factory(Nota, extra=1, fields=['descripcion'])
NotaFormSet2 = formset_factory(NotaForm, extra=3)
