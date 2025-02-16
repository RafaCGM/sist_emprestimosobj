from django.forms import ModelForm
from django.forms import ModelChoiceField
from .models import *
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['matricula','nome','username','telefone','email']

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome','descricao']
