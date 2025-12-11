import datetime
from django.shortcuts import render

# Create your views here.
def mostrar_formulario(request):
    """Muestra la plantilla HTML que contiene el formulario."""
    return render(request, 'Tallerpost/inicio.html')

def pagina_destino(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', 'Invitado')
    else:
        nombre = request.GET.get('nombre', 'Invitado')
    titulo = 'Datos introducidos'
    ahora =datetime.datetime.today()
    fecha = ahora.date().strftime('%d/%m/%Y')
    hora = ahora.time().strftime('%H:%M')
    contexto = {'nombre_usuario': nombre,'fecha_actual': fecha,'hora_actual': hora,'titulo' : titulo}
    return render(request, 'Tallerpost/destino.html', contexto)