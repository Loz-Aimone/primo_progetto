from django.urls import path
from .views import Autore_ALDetailViewCB, Libro_ALListView
app_name="libreria"
urlpatterns = [
    path("autori/<int:pk>", Autore_ALDetailViewCB.as_view(), name="autore_detail"),
    path("lista_libri/", Libro_ALListView.as_view(), name="lista_libri"),
]