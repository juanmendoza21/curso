from applications.home.models import Prueba
from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
)
#import models
from .models import Prueba
class PruebaViews(TemplateView):
    template_name = 'home/prueba.html'

class PruebaViews2(TemplateView):
    template_name = 'home/afil_educ02.php'


class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'ListaNumeros'
    queryset = ['0','10','20','30']

class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model =Prueba
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    fields =['titulo','subtitulo','cantidad']
