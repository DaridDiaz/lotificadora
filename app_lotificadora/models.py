from django.db import models
from django.db.models.fields import DecimalField
from app_lotificadora.views import cliente
from django.contrib.auth.models import User
# Create your models here.

class Cliente(models.Model):
    dni = models.CharField(max_length=35)
    nombrec = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    direccion = models.CharField(max_length=40)
    fecha = models.DateField()
    telefono = models.CharField(max_length=35)
    correo = models.EmailField(max_length=40)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

class Sector(models.Model):
    nombres = models.CharField(max_length=35)
    
class Lote(models.Model):
    nombrel = models.CharField(max_length=35)
    ubicacion = models.CharField(max_length=40)
    dimension = models.CharField(max_length=40)
    cuotas = models.DecimalField(max_digits=4, decimal_places=0)
    precio = DecimalField(max_digits=12, decimal_places=2)
    vendido = models.BooleanField()

class Vendedor(models.Model):
    dni = models.CharField(max_length=35)
    nombrec = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    direccion = models.CharField(max_length=40)
    fecha = models.DateField()
    telefono = models.CharField(max_length=35)
    correo = models.EmailField(max_length=40)

class Cuenta(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    saldo_pagar = models.DecimalField(max_digits=12, decimal_places=2)
    estado = models.BooleanField()
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE, null=True)

class Pago(models.Model):
    MOVIMIENTOS = (
        ('1', 'Pago cuota'),
        ('2', 'Pago a capital'),
    )
    fecha = models.DateTimeField(auto_now_add=True)
    movimiento = models.CharField(max_length=1, choices=MOVIMIENTOS)
    origen = models.ForeignKey(Cuenta, related_name='origen', on_delete=models.CASCADE)
    destino = models.ForeignKey(Cuenta, related_name='destino', on_delete=models.CASCADE, null=True, blank=True)
    monto = models.FloatField(null=True, blank=True)
    comentario = models.TextField(null=True, blank=True)