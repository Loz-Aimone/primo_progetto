from django.db import models

class Giornalista(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    
    def__str__(self):
        return self.nome + " " + self.cognome

class Articolo(models.Model):
    titolo = models.CharField()
    contenuto = models.TextField()
    giornalista = models.ForeignKey(Giornalista, on_delete=models,CASCADE, related_name="articoli")
    
    def__str__(self):
        return self.titolo