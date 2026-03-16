from django.db import models
from django.contrib.auth.models import User


class Lista(models.Model):
    nome = models.CharField(max_length=100, null=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_cricao = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nome

class ConteudoLista(models.Model):
    conteudo = models.CharField(max_length=200)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)

    def __str__(self):
        return self.conteudo
# Create your models here.
