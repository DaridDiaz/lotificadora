from django.test import TestCase

# Create your tests here.
def contrato(request):
    if request.is_ajax() and request.method == 'POST':
        cuota = int(request.POST.get('cbo-cuotas'))
        cliente_n = request.POST.get('cbo-nombre')
        vendedor_n = request.POST.get('cbo-vendedor')
        sector_n = request.POST.get('cbo-sector')
        lote_n = request.POST.get('cbo-lote')

        cliente = Cliente.objects.get(pk=cliente_n)
        vendedor = Cliente.objects.get(pk=vendedor_n)
        sector = Cliente.objects.get(pk=sector_n)
        lote = Cliente.objects.get(pk=lote_n)
        calculo = 1000000/(math.pow(1-(1+0.05),float(cuota))/0.05)

        Contrato.objects.create(
            cliente = cliente,
            vendedor = vendedor,
            sector = sector,
            lote = lote,
            cuota = cuota,
            precio_cuota = calculo,
        )

    cliente = Cliente.objects.all()
    vendedor = Vendedor.objects.all()
    sector = Sector.objects.all()
    lote = Lote.objects.all()
    ctx = {
        'ven': vendedor,
        'cli': cliente,
        'se' : sector,
        'lo' : lote
    }
    return render(request, 'contrato/contrato.html', ctx)