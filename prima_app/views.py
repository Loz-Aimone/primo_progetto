from django.shortcuts import render

# Create your views here.
from  django.http  import  HttpResponse
# Crea le tue visualizzazioni qui.

#L1
def  homepage ( richiesta ):
    return  HttpResponse ( "<h1> Benvenuti nella homepage di Loz Marketing Srl®! </h1>" )

#L2
def menu(request):
    return HttpResponse("<ol><li>Prima opzione</li><li>Seconda opzione</li><li>Terza opzione</li></ol>")
#L3
def chisiamo(request):
    return render(request, "chi_siamo.html")
#L4
def variabili(request):
    context= { 'var1': '2002','var2': 'Aimone Lorenzo', 'var3' : 'Nato a Rho MI'}
    return render(request, "variabili.html",context)
#L5
def index(request):
    return render(request, "index.html")