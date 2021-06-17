from applications import persona
from applications.departamento.models import Departamento
from django.shortcuts import render
import fontawesome as fa
from django.views.generic import (
    ListView   
)
from .models import Empleado
class ListAllEmpleados (ListView):
    template_name ='persona/list_all.html'
    model = Empleado
    context_object_name='lista'

class Listprueba(ListView):
    """ prueba boostrap4"""
    template_name = 'persona/prueba1.html'
    model = Empleado
    context_object_name ='empleados'       

class ListByAreaEmpleado (ListView):
    template_name ='persona/list_by_area.html'
  
    def get_queryset(self):
        area = self.kwargs['name']
        lista = Empleado.objects.filter(
            departamento__name=area
        )
        return lista
class ListEmpleadosByKword(ListView):
    """ lista de empleados por palabra clave"""
    template_name = 'persona/by_kword.html'
    context_object_name ='empleados'
    
    def get_queryset(self):
        print('************************')
        palabra_clave =self.request.GET.get("kword",'')
        lista=Empleado.objects.filter(
            first_name=palabra_clave
        )
       
        return [lista]

#1 Listar todos los empleados de la empresa
#2 Listar todos los empleados que pertenecen a  un area de la empresa
#3 Listar empleados por trabajo
#4 Listar empleados por palabra clave
#5 Listar habilidades de un empleado
