from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Soy el index de la App2</h1>")

def saludo(request):
    html="""
    <h1>Soy la página 1 de la App2</h1>
    <a href="App2/index">Volver</a
    """
    return HttpResponse(html)