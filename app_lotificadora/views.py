from django.shortcuts import render

# Create your views here.
def cliente(request):

    ctx = {}

    return render(request, 'cliente/cliente.html', ctx)