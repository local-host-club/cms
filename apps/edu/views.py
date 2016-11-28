from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from braces.views import LoginRequiredMixin
from apps.edu.models import *
from apps.edu.forms import *


class CompetenciaAreaCreateView(CreateView):
    model = CompetenciaArea
    form_class = CompetenciaAreaForm
    template_name = 'edu/competencia_area_form.html'


class CompetenciaAreaList(ListView):
    model = CompetenciaArea
    template_name = 'edu/competencia_area_list.html'


class CompetenciaCreateView(CreateView):
    model = Competencia
    form_class = CompetenciaForm
    template_name = 'edu/competencia_form.html'


class IndicadorCreateView(CreateView):
    model = Indicador
    form_class = IndicadorForm
    template_name = 'edu/indicador_form.html'


class NivelCreateView(CreateView):
    model = Nivel
    form_class = NivelForm
    template_name = 'edu/nivel_form.html'


class CompetenciaAreaDetail(DetailView):
    model = CompetenciaArea
    template_name = 'edu/competencia_area.html'


class NotaCreateView(DetailView):
    model = Nota
    template_name = 'edu/nota_add.html'

    def get_context_data(self, **kwargs):
        context = super(NotaCreateView, self).get_context_data(**kwargs)
        context['indicador'] = Indicador.objects.get(id=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        obj = Indicador.objects.get(id=self.kwargs['pk'])
        nota_form = NotaFormSet2(self.request.POST)
        for numero, form in enumerate(nota_form):
            form.instance.numero = numero + 1
            form.instance.indicador = obj
            form.save()
        return self.render_to_response({'nota_form': nota_form})

    def get(self, request, *args, **kwargs):
        nota_form = NotaFormSet2()
        return self.render_to_response({'nota_form': nota_form})


class EvaluacionCreateView(LoginRequiredMixin, CreateView):
    model = Evaluacion
    form_class = EvaluacionForm
    template_name = 'edu/evaluacion_add.html'

    def form_valid(self, form):
        form.instance.creada_por = self.request.user
        return super(EvaluacionCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('evaluacion_detail', kwargs={'pk': self.object.id})


class EvaluacionDetail(DetailView):
    template_name = 'edu/evaluacion_detail.html'
    model = Evaluacion


class EvaluacionListView(ListView):
    template_name = 'edu/evaluacion_list.html'
    model = Evaluacion
