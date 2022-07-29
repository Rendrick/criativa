from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do usuario')

    def __str__(self):
        return self.nome