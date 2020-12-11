from django.urls import path
from .views import home, Autore_ALDetailViewCB, Libro_ALListView
app_name="libreria"
urlpatterns = [
    path("",home, name="homeview"),
    #path("articoli/<int:pk>", articoloDetailView, name="articolo_detail")
    path("autori/<int:pk>", Autore_ALDetailViewCB.as_view(), name="autore_detail"),
    path("lista_libri/", Libro_ALListView.as_view(), name="lista_libri"),
]