from django.db import models

# Create your models here.
class Genere_AL(models.Model):
    nome = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome 
    class Meta:
        verbose_name = "Genere"
        verbose_name_plural = "Generi"

class Autore_AL(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.nome + " " + self.cognome
    class Meta:
       verbose_name = "Autore"
       verbose_name_plural = "Autori"

class Libro_AL(models.Model):
    titolo = models.CharField(max_length=80)
    Genere = models.ManyToManyField(Genere_AL)
    Autore = models.ForeignKey(Autore_AL, on_delete=models.CASCADE, related_name="libri")
    ISBN = models.CharField(max_length=15)
    
    def __str__(self):
        return self.titolo 
    class Meta:
       verbose_name = "Libro"
       verbose_name_plural = "Libri"