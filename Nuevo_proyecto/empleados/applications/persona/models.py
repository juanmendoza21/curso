from django.db import models
from django.db.models.fields import DateField
from ckeditor.fields import RichTextField
from applications.departamento.models import Departamento




# Create your models here.
class Habilidades (models.Model):
    habilidad  = models.CharField('Habilidad', max_length=50)
    class meta:    
        verbose_name ='Habilidad'
        verbose_name_plural = 'Habilidades Empleados'


class Empleado (models.Model):
    JOB_CHOICES = (
    ('0','CONTADOR'),
    ('1','ADMINISTRADOR'),
    ('2','ECONOMISTA'),
    ('3','OTROS'),
    )
#1
    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellido', max_length=60)
    job = models.CharField('Trabajo', max_length=1,choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)def __str__(self) :
    nacimiento = models.DateField('Nacimiento', auto_now=False,null=True, auto_now_add=False)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
    class meta:
        verbose_name ='Mi Empleado'
        verbose_name_plural = 'Empleados de la Empresa'
        ordering =['-first_name','last_name']
        unique_together =('first_name','departamento')
    def __str__(self) :
        return str(self.id) +'-'+ self.first_name + '-' + self.last_name