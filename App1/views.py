from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    html="""
    <h1>soy el index de la App1</h1>
    <h2>hola!</h2>
    """
    return HttpResponse(html)

def pagina1(request):
    html="""
    <h1 style="color:blue">Soy la página 1</h1>
    """
    return HttpResponse(html)