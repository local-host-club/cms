"""cms URL Configuration
"""
from django.conf.urls import url
from apps.lh_auth import views

urlpatterns = [
    url(r'^login/$', views.UserLogin.as_view(), name='login'),
    url(r'^signup/$', views.UserSignUp.as_view(), name='signup'),
    url(r'^perfil/(?P<pk>\d+)/$', views.PerfilDetail.as_view(), name='perfil_detail'), ]
