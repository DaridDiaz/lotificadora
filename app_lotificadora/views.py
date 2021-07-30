from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.http import JsonResponse 
from .models import Cuenta, Pago, Cliente, Contrato, Vendedor, Sector

# Create your views here.

def pago(request):
    if request.is_ajax() and request.method == 'POST':
        accion = request.POST.get('cbo-pago')

        if accion == '1': #pago a cuota
            cuenta_id = request.POST.get('cbo-cuenta')
            monto = request.POST.get('txt-monto')

            cuenta = Cuenta.objects.get(pk=cuenta_id)

            cuenta.saldo_pagar -= float(monto)
            cuenta.save()

            Pago.objects.create(
                movimiento = '1',
                origen = cuenta.cliente,
                monto = request.POST.get('txt-monto')

            )
            return JsonResponse({'msj': 'El deposito a sido realizado'})


        elif accion == '2': #pago a capital
            pass

    cuenta = Cuenta.objects.all()
    return render(request, 'pago/pago.html', {'Cuenta': cuenta})


def cliente(request):
    if request.is_ajax() and request.method == 'POST':
        
        Cliente.objects.create(
            dni = request.POST.get('txt-dni'),
            nombre = request.POST.get('txt-nombre'),
            apellido = request.POST.get('txt-apellido'),
            direccion = request.POST.get('txt-direccion'),
            fecha = request.POST.get('txt-fecha'),
            telefono = request.POST.get('txt-telefono'),
            correo = request.POST.get('txt-correo'),
        )
        
    return render(request, 'cliente/cliente.html')

def cliente_tabla(request):
    if request.method == 'POST' and request.is_ajax():
        return HttpResponse ('')
    else:
        raise Http404('Not Found')

def vendedor(request):

    ctx = {}

    return render(request, 'vendedor/vendedor.html', ctx)