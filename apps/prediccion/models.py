# from django.db import models
from mongoengine import *
from proyecto2.settings import DBNAME
# Create your models here.

connect(DBNAME)

class data(Document):
    Periodo = StringField(max_length=300)
    Nivel = StringField(max_length=300)
    Seccion = StringField(max_length=300)
    Apellido = StringField(max_length=300)
    Nombre = StringField(max_length=300)
    Sexo = StringField(max_length=300)
    Facultad = StringField(max_length=300)
    Carrera = StringField(max_length=300)
    Socioeconomico = StringField(max_length=300)
    PromedioAsis = FloatField(default='0.0')
    Promedionota = FloatField(default='0.0')


    # def _unicode_(self):
    #     return "%s" %(self.Periodo)