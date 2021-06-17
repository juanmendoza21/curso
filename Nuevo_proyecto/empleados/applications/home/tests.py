from django.test import TestCase

# Create your tests here.
from django.views.generic import TemplateView

class PruebaView(TemplateView):
    template_name ='prueba.html'