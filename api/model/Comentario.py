from django.db import models
from django.contrib.auth.models import User
from api.model.Postagem import Postagem
from django.utils import timezone


class Comentario(models.Model):
    user = models.ForeignKey(User, related_name= 'comentou', on_delete = models.CASCADE)
    postagem = models.ForeignKey(Postagem, related_name= 'comentado', on_delete = models.CASCADE)
    texto = models.TextField(default="")
    data_criada = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user + "\n" + self.texto + "\n" + self.data_criada