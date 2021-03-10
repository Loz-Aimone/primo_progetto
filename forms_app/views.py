from django.shortcuts import render
from .forms import formContatto

def contatti(request):
    form = formContatto()
    context = {"form": form}
    return render(request, "contatto.html", context)
