from django.shortcuts import render

# Create your views here.
def mostrar_html(request):
    return render(request, 'gestion_inventarios.html')