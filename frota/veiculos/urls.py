from django.conf.urls import url
from frota.veiculos import views


app_name='veiculos'

urlpatterns = [
    url(r'^lista-departamento/$',views.lista_departamento, name='lista-departamentos'),
    url(r'^lista-responsaveis/$',views.lista_responsaveis, name='lista-responsaveis'),
    #url(r'^deleta-departamento/(?P<id_departamento>[0-9]+)/$',views.deleta_departamento, name='deleta_departamento'),
    url(r'^deleta-departamento/(?P<id_departamento>)/$',views.deleta_departamento, name='deleta_departamento'),
    url(r'^novo-responsavel/$',views.novo_responsavel, name='novo-responsavel'),
    url(r'^novo-departamento/$',views.novo_departamento, name='novo-departamento'),
]

