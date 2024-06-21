from django.shortcuts import render, redirect

# Create your views here.
from .models import Clientes
from .forms import ClienteForm

def gestion_clientes(request):
    clientes = Clientes.objects.all()
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/gestion_clientes.html', {'clientes': clientes, 'form': form})