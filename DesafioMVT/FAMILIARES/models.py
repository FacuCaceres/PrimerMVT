from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField(max_length=2)
    nacimiento = models.DateTimeField()

    def __str__(self):
        return f' NOMBRE : {self.nombre} EDAD : {self.edad} NACIMIENTO : {self.nacimiento}'