
from django.contrib import admin
from django.urls import path
import fontawesome as fa

print(fa.icons['thumbs-up'])

from . import views
urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('lista_by_area/<name>/', views.ListByAreaEmpleado.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('prueba1/', views.Listprueba.as_view()),
]

