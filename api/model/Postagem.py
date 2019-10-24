from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Postagem(models.Model):
    user = models.ForeignKey(User, related_name= 'autor', on_delete = models.CASCADE)
    texto = models.TextField(default="")
    data_criada = models.DateTimeField(default=timezone.now)
    numeroLikes = models.IntegerField(default=0)
    numeroComentarios = models.IntegerField(default=0)
    numeroRts = models.IntegerField(default=0)

    def __str__(self):
        return self.user + "\n" + self.texto + "\n" + self.data_criada + "\n" + self.numeroComentarios + " " + self.numeroRts + " " + self.numeroLikes
