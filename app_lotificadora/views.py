from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.http import JsonResponse 
from .models import Cuenta, Cliente, Sector, Vendedor, Contrato

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

    ctx = {}
    return render(request, 'cliente/cliente.html', ctx)

def cliente_tabla(request):
    if request.method == 'POST' and request.is_ajax():
        return HttpResponse ('')
    else:
        raise Http404('Not Found')

def contrato(request):
    if request.is_ajax() and request.method == 'POST':
        Contrato.objects.create(
            cliente = request.POST.get('txt-nombre'),
            vendedor = request.POST.get('cbo-vendedor'),
            sector = request.POST.get('cbo-vendedor'),
            lote = request.POST.get('cbo-vendedor'),
            cuota = request.POST.get('txt-cuota'),
            precio_cuota = request.POST.get('txt-Precio'),
        )

    cliente = Cliente.objects.all()
    vendedor = Vendedor.objects.all()
    ctx = {
        'ven': vendedor,
        'cli': cliente
    }
    return render(request, 'contrato/contrato.html', ctx)