from django.db import models


class Loja(models.Model):
    nome = nome = models.CharField(max_length=100, help_text='Nome da Loja')

    def __str__(self):
        return self.nome
