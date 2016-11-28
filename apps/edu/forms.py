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


class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = ['nombre', 'estrategia', 'indicador']
        labels = {
            'indicador': 'Indicadores de logro'}
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'estrategia': forms.Textarea(attrs={'class': 'form-control'}),
            'indicador': forms.CheckboxSelectMultiple()}

    def save(self, commit=True):
        instance = super(EvaluacionForm, self).save(commit=False)
        instance.save()
        EvaluacionIndicador.objects.filter(evaluacion=instance).delete()
        for ind in self.cleaned_data['indicador']:
            ev_indicador = EvaluacionIndicador(evaluacion=instance, indicador=ind)
            ev_indicador.save()


NotaFormSet = modelformset_factory(Nota, extra=1, fields=['descripcion'])
NotaFormSet2 = formset_factory(NotaForm, extra=8)
