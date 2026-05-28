from django.db import models
from django.contrib.auth.models import User

class Contato(models.Model):

    nome = models.CharField(max_length=100)

    email = models.EmailField()

    assunto = models.CharField(max_length=200)

    mensagem = models.TextField()

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    comentario = models.TextField()

    nota = models.IntegerField()

    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username
