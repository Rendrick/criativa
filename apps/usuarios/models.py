from django.db import models
from django.contrib.auth.models import User
from apps.lojas.models import Loja
from apps.auditorias.models import Auditorias

class Usuario(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do usuario')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    lojas = models.ManyToManyField(Loja)
    auditoria = models.ForeignKey(Auditorias, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome