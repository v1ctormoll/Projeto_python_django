from django.db import models

# Create your models here.

class Produtos(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    data = models.DateTimeField()

    def __str__(self):
        return self.nome
