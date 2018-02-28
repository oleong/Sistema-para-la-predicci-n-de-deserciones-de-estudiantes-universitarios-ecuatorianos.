from django.conf.urls import patterns, include, url

from .views import index, datos, predecir, graficos, agregaDatos, consultaDatos, predecirDatos



urlpatterns = [
    # Examples:
    # url(r'^$', 'tesis.views.home', name='home'),
     url(r'^index/$', index.as_view(), name='index'),
     url(r'^datos/$', datos.as_view(), name='datos'),
     url(r'^predecir/$', predecir.as_view(), name='predecir'),
     url(r'^graficos/$', graficos.as_view(), name='graficos'),
     url(r'^agregardatos/$', agregaDatos, name='agregardatos'),
     url(r'^extraer_datos/$', consultaDatos.as_view(), name="consultadatos"),
     url(r'^predecir_datos/$', predecirDatos.as_view(), name="predecirdatos"),

]
