from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse
from math import pow 
from .models import Cliente, Vendedor, Cuenta, Sector, Contrato, Lote

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def pago(request):
    c = Cuenta.objects.all()
    if request.is_ajax() and request.method == 'POST':
        accion = request.POST.get('cbo-pago')

        if accion == '1': #pago a cuota
            cuenta_id = request.POST.get('cbo-cuenta')
            cuenta = Cuenta.objects.get(pk=cuenta_id)
            #cuentas = get_object_or_404(Contrato, pk=request.POST.get('cbo-cuenta'))

            cuotas = 80000
            saldo = 800000
            interes = float(saldo)*(0.1)
            capital = float(cuotas) - float(interes)

            cuenta.saldo_pagar -= float(capital)
            cuenta.save()

            return JsonResponse({'msj': 'El deposito a sido realizado'})
        elif accion == '2': #pago a capital
            return JsonResponse({'msj': 'El deposito a sido realizado'})
            pass

    ctx = {
        'Cuenta': c,
    }
    return render(request, 'pago/pago.html', ctx)

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
    lo = Lote.objects.all()
    se = Sector.objects.all()
    
    

    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, pk=request.POST.get('cbo-cliente'))
        vendedor = get_object_or_404(Vendedor, pk=request.POST.get('cbo-vendedor'))
        lote = get_object_or_404(Lote, pk=request.POST.get('cbo-lote'))
        cuotas = request.POST.get('cbo-cuotas')
        prima = request.POST.get('txt-prima')

        lote.precio -= float(prima)
        lote.save()

        Cuenta.objects.create(saldo_pagar=lote.precio,cliente=cliente)

        cuotas = cuotas
        tasa = 10/100
        monto = lote.precio
        precio_cuota = (float(monto))/((1-(1+tasa)** -float(cuotas))/tasa)

        Contrato.objects.create(cliente=cliente,vendedor=vendedor,lote=lote,cuotas=int(cuotas),precio_cuota=float(precio_cuota))
        
        lote.estado=(False)
        lote.save()
        messages.add_message(request, messages.INFO, 'El contrato se ha creado de forma exitosa')
    
    ctx = {
        'cliente': cli,
        'vendedor': ven,
        'lote' : lo,
        'sector': se,
    }
    return render(request, 'contrato/contrato.html', ctx)

def terreno(request):
    # lote = Lote.objects.all().order_by('nombre')
    # ctx = {
    #     'lote': lote
    # }
    # return render(request, 'terreno/terreno.html')

    q = request.GET.get('q')
    if q:
        sec = Sector.objects.filter(nombre__startswith=q).order_by('nombre')
        lot = Lote.objects.filter(nombre__startswith=q).order_by('nombre')
    else:
        sec = Sector.objects.all().order_by('nombre')
        lot = Lote.objects.all().order_by('nombre')
    #POST
    if request.method == 'POST':
        nombre = request.POST.get('txt-nombre')
        cantidad = request.POST.get('txt-cantidad')
        ubicacion = request.POST.get('txt-ubicacion')

        Sector.objects.create(nombre=nombre,cantidad=cantidad,ubicacion=ubicacion)
        
        messages.add_message(request, messages.INFO, f'El Sector {nombre} se ha registrado de forma exitosa')


    ctx = {

        'terreno': sec,
        'terreno': lot,
    }

    return render(request, 'terreno/terreno.html', ctx)

def lote(request):
    if request.method == 'POST':
        nombre = request.POST.get('txt-nombre')
        sector = request.POST.get('cbo-sector')
        dimension = request.POST.get('txt-dimension')
        precio = request.POST.get('txt-precio')
        estado = request.POST.get('chk-estado')

        Lote.objects.create(nombre=nombre,sector=sector,dimension=dimension,precio=precio,estado=estado)
        
        messages.add_message(request, messages.INFO, f'El Lote {nombre}, sector {sector} se ha registrado de forma exitosa')

def eliminar_terreno(request, id):
    Lote.objects.get(pk=1).delete()
    return redirect(reverse('terreno'))
    # try:
    #     lo = Lote.objects.get(pk=1).delete()(writer=request.user)
    #     if lo:
    #         return render(request, 'terreno/terreno.html', {'lo': lo})   
    # except ObjectDoesNotExist:
    #     return render(request, 'terreno/terreno.html'')