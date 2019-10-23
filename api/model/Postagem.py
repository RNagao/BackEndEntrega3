from django.db import models
from django.utils import timezone


class Postagem(models.Model):
    autor = models.CharField(max_length=20)
    texto = models.TextField()
    data_criada = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.autor
