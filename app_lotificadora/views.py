from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from math import pow 
from .models import Cliente, Vendedor, Cuenta, Sector, Contrato, Lote

# Create your views here.

def index(request):
    return HttpResponse('login en proceso')

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

def vendedor(request):
    q = request.GET.get('q')
    if q:
        ven = Vendedor.objects.filter(nombre__startswith=q).order_by('nombre')
    else:
        ven = Vendedor.objects.all().order_by('nombre')
    #POST
    if request.method == 'POST':
        dni = request.POST.get('txt-dni')
        nombre = request.POST.get('txt-nombre')
        apellido = request.POST.get('txt-apellido')
        direccion = request.POST.get('txt-direccion')
        fecha = request.POST.get('txt-fecha')
        telefono = request.POST.get('txt-telefono')
        correo = request.POST.get('txt-correo')

        Vendedor.objects.create(dni=dni,nombre=nombre,apellido=apellido,direccion=direccion,fecha=fecha,telefono=telefono,correo=correo)
        
        messages.add_message(request, messages.INFO, f'El Empleado {nombre} {apellido} se ha registrado de forma exitosa')

    ctx = {
        'vendedor': ven,
    }
    return render(request, 'vendedor/vendedor.html', ctx)

def mantenimiento_vendedor(request, id):
    v = get_object_or_404(Vendedor, pk=id)
    ven = Vendedor.objects.all().order_by('nombre')
    #POST
    if request.method == 'POST':
        dni = request.POST.get('txt-dni')
        nombre = request.POST.get('txt-nombre')
        apellido = request.POST.get('txt-apellido')
        direccion = request.POST.get('txt-direccion')
        fecha = request.POST.get('txt-fecha')
        telefono = request.POST.get('txt-telefono')
        correo = request.POST.get('txt-correo')

        v = Vendedor.objects.get(pk=id)
        v.dni = dni
        v.nombre = nombre
        v.apellido = apellido
        v.direccion = direccion
        v.fecha = fecha
        v.telefono = telefono
        v.correo = correo
        v.save()
        
        messages.add_message(request, messages.INFO, f'El Empleado {nombre} {apellido} se ha actualizado de forma exitosa')

    ctx = {
            'vendedor': ven,
            'v': v
        }
    return render(request, 'vendedor/vendedor.html', ctx)

def cliente(request):
    q = request.GET.get('q')
    if q:
        cli = Cliente.objects.filter(nombre__startswith=q).order_by('nombre')
    else:
        cli = Cliente.objects.all().order_by('nombre')
    #POST
    if request.method == 'POST':
        dni = request.POST.get('txt-dni')
        nombre = request.POST.get('txt-nombre')
        apellido = request.POST.get('txt-apellido')
        direccion = request.POST.get('txt-direccion')
        fecha = request.POST.get('txt-fecha')
        telefono = request.POST.get('txt-telefono')
        correo = request.POST.get('txt-correo')

        Cliente.objects.create(dni=dni,nombre=nombre,apellido=apellido,direccion=direccion,fecha=fecha,telefono=telefono,correo=correo)
        
        messages.add_message(request, messages.INFO, f'el cliente {nombre} {apellido} se ha registrado de forma exitosa')

    ctx = {
        'cliente': cli,
    }
    return render(request, 'cliente/cliente.html', ctx)

def mantenimiento_cliente(request, id):
    c = get_object_or_404(Cliente, pk=id)
    cli = Cliente.objects.all().order_by('nombre')
    #POST
    if request.method == 'POST':
        dni = request.POST.get('txt-dni')
        nombre = request.POST.get('txt-nombre')
        apellido = request.POST.get('txt-apellido')
        direccion = request.POST.get('txt-direccion')
        fecha = request.POST.get('txt-fecha')
        telefono = request.POST.get('txt-telefono')
        correo = request.POST.get('txt-correo')

        c = Cliente.objects.get(pk=id)
        c.dni = dni
        c.nombre = nombre
        c.apellido = apellido
        c.direccion = direccion
        c.fecha = fecha
        c.telefono = telefono
        c.correo = correo
        c.save()
        
        messages.add_message(request, messages.INFO, f'el cliente {nombre} {apellido} se ha actualizado de forma exitosa')

    ctx = {
            'cliente': cli,
            'c': c
        }
    return render(request, 'cliente/cliente.html', ctx)

def contrato(request):
    cli = Cliente.objects.all()
    ven = Vendedor.objects.all()
    sec = Sector.objects.all()
    lo = Lote.objects.all()
    
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, pk=request.POST.get('cbo-cliente'))
        vendedor = get_object_or_404(Vendedor, pk=request.POST.get('cbo-vendedor'))
        lote = get_object_or_404(Lote, pk=request.POST.get('cbo-lote'))
        cuotas = request.POST.get('cbo-cuotas')
        precio = request.POST.get('txt-precio')

        Contrato.objects.create(cliente=cliente,vendedor=vendedor,lote=lote,cuotas=int(cuotas),precio_cuota=float(precio))
    

    ctx = {
        'cliente': cli,
        'vendedor': ven,
        'sector' : sec,
        'lote' : lo,
    }
    return render(request, 'contrato/contrato.html', ctx)

def terreno(request):
    return render(request, 'terreno/terreno.html')