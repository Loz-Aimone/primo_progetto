from django.shortcuts import render, get_object_or_404
from .models import Libro_AL, Autore_AL
from django.views.generic.detail import DetailView 
from django.views.generic.list import ListView
def home(request):
    libri = Libro.objects.all()
    autori = Autore.objects.all()
    context = {"libri": libri, "autori": autori}
    print(context)
    return render(request, "homepage.html", context)

class LibroListView(ListView):
    model = Libro
    template_name = "lista_libri.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["libri"] = Libro.objects.all()
        return context

class AutoreDetailViewCB(DetailView):
    model = Autore
    template_name = "autore_detail.html"


