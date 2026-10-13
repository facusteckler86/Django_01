from django.http import HttpResponse

def saludar(request):
    return HttpResponse("<h1>Hola a todos</h1>")