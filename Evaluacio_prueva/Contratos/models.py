from django.db import models

# Create your models here.
class Empleados(models.Model):
    cedula_empleados = models.IntegerField(max_length=10, blank=False, primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    puesto = models.CharField(max_length=50)
def _str_(self):
     return self.nombre
class candidatos(models.Model):
     cedula_candidatos = models.IntegerField(max_length=10, blank=False, primary_key=True)
     nombre=models.CharField(max_length=20)
     apellido=models.CharField(max_length=30)
     fecha_nacimiento=models.DateField()
     direccion=models.CharField(max_length=100)
     telefono=models.CharField(max_length=10)
     
def str(self):
     return self .nombre
class Posiciones(models.Model):
     cedula_pocisiones=models.IntegerField(max_length=10, blank=False, primary_key=True)
     nombre_posicion=models.CharField(max_length=50)
     puesto=models.CharField(max_length=50)
     salario=models.DecimalField(max_digits=8, decimal_places=2)
def str(self):
     return self .nombre
class Contrataciones(models.Model):
     cedula_contrataciones=models.IntegerField(max_length=10, blank=False, primary_key=True)
     cedula_candidatos=models.ForeignKey(candidatos, on_delete=models.RESTRICT)
     cedula_pocisiones=models.ForeignKey(Posiciones, on_delete=models.RESTRICT)
     fecha_inicio=models.DateField()
     fecha_fin=models.DateField()
def _str_(self):
     return self .cedula_contratacion
