from django.db import models

# Create your models here.
class Auditorias(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da Auditoria')

    def __str__(self):
        return self.nome