from django.db import models
from django.contrib.auth.models import User
from api.model.Postagem import Postagem


class Curtida(models.Model):
    user = models.ForeignKey(User, related_name= 'curtiu', on_delete = models.CASCADE)
    postagem = models.ForeignKey(Postagem, related_name= 'curtida', on_delete = models.CASCADE)

    def __str__(self):
        return self.user