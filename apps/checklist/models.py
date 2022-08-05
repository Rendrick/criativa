from django.db import models
from apps.lojas.models import Loja
from apps.usuarios.models import Usuario


class CheckList(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Loja, on_delete=models.SET_NULL, null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao