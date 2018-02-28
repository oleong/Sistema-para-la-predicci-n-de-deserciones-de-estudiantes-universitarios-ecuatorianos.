# -*- encoding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, View
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
import json
from .models import data

class index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data(**kwargs)
        total = data.objects.filter(Periodo = 'OCTUBRE 2017- MARZO 2018').count()
        total1 = data.objects.filter(Periodo = 'MAYO A SEPTIEMBRE 2015').count()
        total2 = data.objects.filter(Periodo = 'OCTUBRE 2015 A  MARZO 2016').count()
        total3 = data.objects.filter(Periodo = 'MAYO A  SEPTIEMBRE 2016').count()
        total4 = data.objects.filter(Periodo = 'OCTUBRE 2016  MARZO 2017').count()
        total5 = data.objects.filter(Periodo = 'ABRIL A SEPTIEMBRE 2017').count()
        socioeconomicoa = data.objects.filter(Socioeconomico = 'ALTO', Periodo = 'OCTUBRE 2017- MARZO 2018').count()
        socioeconomico = data.objects.filter(Socioeconomico = 'D BAJO', Periodo = 'OCTUBRE 2017- MARZO 2018').count()
        socioeconomico1 = data.objects.filter(Socioeconomico = 'D BAJO', Periodo = 'MAYO A SEPTIEMBRE 2015').count()
        socioeconomico2= data.objects.filter(Socioeconomico = 'D BAJO', Periodo = 'OCTUBRE 2015 A  MARZO 2016').count()
        socioeconomico3 = data.objects.filter(Socioeconomico = 'D BAJO', Periodo = 'MAYO A  SEPTIEMBRE 2016').count()
        socioeconomico4 = data.objects.filter(Socioeconomico = 'D BAJO', Periodo = 'OCTUBRE 2016  MARZO 2017').count()
        socioeconomico5 = data.objects.filter(Socioeconomico = 'D BAJO', Periodo = 'ABRIL A SEPTIEMBRE 2017').count()


        context['total'] = total
        context['total1'] = total1
        context['total2'] = total2
        context['total3'] = total3
        context['total4'] = total4
        context['total5'] = total5
        context['socioeconomicoa'] = socioeconomicoa
        context['socioeconomico1'] = socioeconomico1
        context['socioeconomico2'] = socioeconomico2
        context['socioeconomico3'] = socioeconomico3
        context['socioeconomico4'] = socioeconomico4
        context['socioeconomico5'] = socioeconomico5
        context['socioeconomico'] = socioeconomico

        return context

class datos(TemplateView):
    template_name = 'datos.html'

class graficos(TemplateView):
    template_name = 'graficos.html'

    def get_context_data(self, **kwargs):
        context = super(graficos, self).get_context_data(**kwargs)
        total = data.objects.filter(Periodo='OCTUBRE 2017- MARZO 2018').count()
        total1 = data.objects.filter(Periodo='MAYO A SEPTIEMBRE 2015').count()
        total2 = data.objects.filter(Periodo='OCTUBRE 2015 A  MARZO 2016').count()
        total3 = data.objects.filter(Periodo='MAYO A  SEPTIEMBRE 2016').count()
        total4 = data.objects.filter(Periodo='OCTUBRE 2016  MARZO 2017').count()
        total5 = data.objects.filter(Periodo='ABRIL A SEPTIEMBRE 2017').count()
        socioeconomicoa = data.objects.filter(Socioeconomico='ALTO', Periodo='OCTUBRE 2017- MARZO 2018').count()
        socioeconomico = data.objects.filter(Socioeconomico='D BAJO', Periodo='OCTUBRE 2017- MARZO 2018').count()
        socioeconomico1 = data.objects.filter(Socioeconomico='D BAJO', Periodo='MAYO A SEPTIEMBRE 2015').count()
        socioeconomico2 = data.objects.filter(Socioeconomico='D BAJO', Periodo='OCTUBRE 2015 A  MARZO 2016').count()
        socioeconomico3 = data.objects.filter(Socioeconomico='D BAJO', Periodo='MAYO A  SEPTIEMBRE 2016').count()
        socioeconomico4 = data.objects.filter(Socioeconomico='D BAJO', Periodo='OCTUBRE 2016  MARZO 2017').count()
        socioeconomico5 = data.objects.filter(Socioeconomico='D BAJO', Periodo='ABRIL A SEPTIEMBRE 2017').count()

        socioeconomicoa1 = data.objects.filter(Socioeconomico='ALTO', Periodo='MAYO A SEPTIEMBRE 2015').count()
        socioeconomicoa2 = data.objects.filter(Socioeconomico='ALTO', Periodo='OCTUBRE 2015 A  MARZO 2016').count()
        socioeconomicoa3 = data.objects.filter(Socioeconomico='ALTO', Periodo='MAYO A  SEPTIEMBRE 2016').count()
        socioeconomicoa4 = data.objects.filter(Socioeconomico='ALTO', Periodo='OCTUBRE 2016  MARZO 2017').count()
        socioeconomicoa5 = data.objects.filter(Socioeconomico='ALTO', Periodo='ABRIL A SEPTIEMBRE 2017').count()

        context['total'] = total
        context['total1'] = total1
        context['total2'] = total2
        context['total3'] = total3
        context['total4'] = total4
        context['total5'] = total5
        context['socioeconomico1'] = socioeconomico1
        context['socioeconomico2'] = socioeconomico2
        context['socioeconomico3'] = socioeconomico3
        context['socioeconomico4'] = socioeconomico4
        context['socioeconomico5'] = socioeconomico5
        context['socioeconomico'] = socioeconomico
        context['socioeconomicoa'] = socioeconomicoa
        context['socioeconomicoa1'] = socioeconomicoa1
        context['socioeconomicoa2'] = socioeconomicoa2
        context['socioeconomicoa3'] = socioeconomicoa3
        context['socioeconomicoa4'] = socioeconomicoa4
        context['socioeconomicoa5'] = socioeconomicoa5


        return context

class predecir(TemplateView):
    template_name = 'predecir.html'

class consultaDatos(View):

    def get(self, request, *args, **kwargs):

        query = data.objects.filter(Periodo=request.GET['Anio'], Nivel=request.GET['Nivel'], Carrera=request.GET['Carrera'])
        print(query.count())
        context = []
        for datos in query:
            json = { "Nombre": datos.Nombre,
                     "Apellido": datos.Apellido,
                     "PromedioAsis": datos.PromedioAsis,
                     "Promedionota": datos.Promedionota,
                     "Socioeconomico": datos.Socioeconomico,

            }

            context.append(json)
        return JsonResponse(context, safe=False)


class predecirDatos(View):

    def get(self, request, *args, **kwargs):

        query = data.objects.filter(Periodo=request.GET['Anio'], Nivel=request.GET['Nivel'], Carrera=request.GET['Carrera'])
        context = []
        for datos in query:
            result = promedio(datos.Apellido,datos.Nombre)

            json = { "Nombre": datos.Nombre,
                     "Apellido": datos.Apellido,
                     "Promedio": result,
            }
            context.append(json)
        return JsonResponse(context, safe=False)


def promedio(apellido,nombre):
    estudiante = data.objects.filter(Nombre=nombre, Apellido=apellido)
    promAsis = 0.0
    promNot = 0.0
    asistencia = 0.0
    nota = 0.0
    mediaASIS = 87.9
    mediaNOTA = 77.8
    tasis = 0.0
    tnota =0.0
    cont = 0


    for x in estudiante:
        if x.Periodo != 'OCTUBRE 2017- MARZO 2018':
            asistencia = asistencia + x.PromedioAsis
            nota = nota + x.Promedionota
            estado=x.Socioeconomico
            cont = cont + 1
    promAsis = asistencia/cont
    promNot = nota/cont
    print(promAsis,promNot)
    tasis = promAsis/mediaASIS
    tnota = promNot/mediaNOTA
    print(tasis,tnota)
    asistencia = 0.0
    nota = 0.0

    if estado == 'D BAJO' or estado == 'C- MEDIO BAJO':
        if tasis < 1 and tnota < 1:
            resultado = '<span class="label label-danger">Peligro</span>'
        elif tasis < 1 and tnota >= 1:
            resultado = '<span class="label label-warning">Alerta</span>'
        elif tasis >= 1 and tnota < 1:
            resultado = '<span class="label label-warning">Alerta</span>'
        elif tasis >= 1 and tnota >= 1:
            resultado = '<span class="label label-success">Bien</span>'

    if estado == 'C+ MEDIO TIPICO' or estado == 'B MEDIO ALTO':
        if tasis < 1 and tnota < 1:
            resultado = '<span class="label label-danger">Peligro</span>'
        elif tasis < 1 and tnota >= 1:
            resultado = '<span class="label label-success">Bien</span>'
        elif tasis >= 1 and tnota < 1:
            resultado = '<span class="label label-warning">Alerta</span>'
        elif tasis >= 1 and tnota >= 1:
            resultado = '<span class="label label-success">Bien</span>'

    if estado == 'ALTO':
        if tasis < 1 and tnota < 1:
            resultado = '<span class="label label-warning">Alerta</span>'
        elif tasis < 1 and tnota >= 1:
            resultado = '<span class="label label-success">Bien</span>'
        elif tasis >= 1 and tnota < 1:
            resultado = '<span class="label label-Success">Bien</span>'
        elif tasis >= 1 and tnota >= 1:
            resultado = '<span class="label label-success">Bien</span>'


    return resultado


def agregaDatos(request):

        j = json.loads(open('/Users/oscarleon/Desktop/proyecto2/apps/prediccion/datosj.json').read())

        for ja in j:
            data.objects.create(
                Periodo= ja['Periodo'],
                Nivel= ja['Nivel'],
                Seccion= ja['Seccion'],
                Apellido= ja['Apellido'],
                Nombre= ja['Nombre'],
                Sexo= ja['Nombre'],
                Facultad= ja['Facultad'],
                Carrera= ja['Carrera'],
                Socioeconomico= ja['Socioeconomico'],
                PromedioAsis= ja['PromedioAsis'],
                Promedionota= ja['Promedionota'],
            )


