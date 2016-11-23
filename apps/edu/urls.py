"""cms URL Configuration
"""
from django.conf.urls import url
from apps.edu import views

urlpatterns = [
    url(r'^competencia_area/add$', views.CompetenciaAreaCreateView.as_view(), name='competencia_area_add'),
    url(r'^competencia_area/(?P<pk>\d+)/$', views.CompetenciaAreaDetail.as_view(), name='competencia_area_detail'),
    url(r'^competencia/add$', views.CompetenciaCreateView.as_view(), name='competencia_add'),
    url(r'^indicador/add$', views.IndicadorCreateView.as_view(), name='indicador_add'),
    url(r'^nivel/add$', views.NivelCreateView.as_view(), name='nivel_add'),
    url(r'^nota/(?P<pk>\d+)/add$', views.NotaCreateView.as_view(), name='nota_add'), ]
