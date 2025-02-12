from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    matricula = models.IntegerField('Matricula', primary_key=True)
    nome = models.CharField('Nome', max_length=300)
    telefone = models.CharField('Telefone', max_length=12)
    email = models.CharField('Email', max_length=200, unique = True)

    REQUIRED_FIELDS = ['nome','username']
    USERNAME_FIELD = 'email'


    def __str__(self):
        return self.nome 

class Categoria(models.Model):
    nome = models.CharField('Categoria', max_length=200)
    descricao = models.CharField('Descrição', max_length=300)

    def __str__(self):
        return self.nome

class Objeto(models.Model):
    nome = models.CharField('Nome', max_length=300)
    descricao = models.CharField('Descrição', max_length=300)
    dataCadastro = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    objeto = models.ForeignKey(Objeto, on_delete=models.PROTECT)
    dataEmprestimo = models.DateTimeField()
    dataDevolucao = models.DateTimeField(null=True)

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    objeto = models.ForeignKey(Objeto, on_delete=models.PROTECT)
    dataReserva = models.DateTimeField()
    dataAtendimento = models.DateTimeField()