from django.db import models
from django.contrib.auth.models import User
from api.model.Postagem import Postagem


class Compartilhamento(models.Model):
    user = models.ForeignKey(User, related_name= 'compartilhou', on_delete = models.CASCADE)
    postagem = models.ForeignKey(Postagem, related_name= 'compartilhado', on_delete = models.CASCADE)

    def __str__(self):
        return self.user