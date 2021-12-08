from django.db import models

# Create your models here.
class Chamado(models.Model):
    titulo = models.CharField(max_length=100, null=True)
    descricao = models.TextField(max_length=255, null=True)
    foto = models.FileField(upload_to="%Y/%m/%d/", null=True, blank=True)
    setor = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    usuabr = models.CharField(max_length=100, null=True)
    usures = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.descricao

class Setor(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100, null=True)