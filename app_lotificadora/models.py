from django.db import models
from django.db.models.fields import DecimalField

from django.contrib.auth.models import User
# Create your models here.

class Cliente(models.Model):
    dni = models.CharField(max_length=16)
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    direccion = models.TextField()
    fecha = models.DateField()
    telefono = models.CharField(max_length=13)
    correo = models.EmailField(max_length=40)
    fecha_ingreso = models.DateField(auto_now_add=True, null=True)
    estado = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Vendedor(models.Model):
    dni = models.CharField(max_length=16)
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    direccion = models.TextField()
    fecha = models.DateField()
    telefono = models.CharField(max_length=13)
    correo = models.EmailField(max_length=40)
    fecha_ingreso = models.DateField(auto_now_add=True, null=True)
    estado = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Sector(models.Model):
    nombre = models.CharField(max_length=35)
    cantidad = models.FloatField(default=0, null=True, blank=True)
    ubicacion = models.CharField(max_length=40, null=True)
    def __str__(self):
        return self.nombre
    
class Lote(models.Model):
    nombre = models.CharField(max_length=35)
    sector = models.ForeignKey(Sector,on_delete=models.CASCADE, null=True)
    dimension = models.CharField(max_length=40, null=True, blank=True)
    precio = models.FloatField(default=0, null=True, blank=True)
    estado = models.BooleanField(null=True, blank=True)
    def __str__(self):
        return f'{self.sector} - {self.nombre}'

class Cuenta(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    saldo_pagar = models.FloatField(default=0)
    estado = models.BooleanField(default=True)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE, null=True)
    lote = models.ForeignKey(Lote,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.id} {self.cliente} - {self.saldo_pagar}'

class Contrato(models.Model):

    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE, null=True)
    vendedor = models.ForeignKey(Vendedor,on_delete=models.CASCADE, null=True)
    lote = models.ForeignKey(Lote,on_delete=models.CASCADE, null=True)
    cuotas = models.IntegerField(default=0)
    precio_cuota = models.FloatField(default=0)
    cuenta = models.ForeignKey(Cuenta,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.id} {self.cliente} - Cuotas: {self.cuotas}'

class Pago(models.Model):
    MOVIMIENTOS = (
        ('1', 'Pago cuota'),
        ('2', 'Pago a capital'),
    )
    fecha = models.DateTimeField(auto_now_add=True)
    movimiento = models.CharField(max_length=1, choices=MOVIMIENTOS)
    origen = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    monto = models.FloatField(null=True, blank=True)


