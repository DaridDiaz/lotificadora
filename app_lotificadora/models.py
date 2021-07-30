from django.db import models
from django.db.models.fields import DecimalField

from django.contrib.auth.models import User
# Create your models here.

class Cliente(models.Model):
    dni = models.CharField(max_length=35)
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    direccion = models.TextField()
    fecha = models.DateField()
    telefono = models.CharField(max_length=35)
    correo = models.EmailField(max_length=40)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Sector(models.Model):
    nombre = models.CharField(max_length=35)
    
class Lote(models.Model):
    nombre = models.CharField(max_length=35)
    sector = models.ForeignKey(Sector,on_delete=models.CASCADE, null=True)
    ubicacion = models.CharField(max_length=40)
    dimension = models.CharField(max_length=40)
    cuotas = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    vendido = models.BooleanField()

class Vendedor(models.Model):
    dni = models.CharField(max_length=35)
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    direccion = models.CharField(max_length=40)
    fecha = models.DateField()
    telefono = models.CharField(max_length=35)
    correo = models.EmailField(max_length=40)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Cuenta(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    saldo_pagar = models.FloatField(default=0)
    estado = models.BooleanField(default=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f'{self.id} {self.cliente} - {self.saldo_pagar}'

class Pago(models.Model):
    MOVIMIENTOS = (
        ('1', 'Pago cuota'),
        ('2', 'Pago a capital'),
    )
    fecha = models.DateTimeField(auto_now_add=True)
    movimiento = models.CharField(max_length=1, choices=MOVIMIENTOS)
    origen = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    monto = models.FloatField(null=True, blank=True)
    comentario = models.TextField(null=True, blank=True)