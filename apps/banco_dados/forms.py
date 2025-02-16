from django.forms import ModelForm
from django.forms import ModelChoiceField
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome','descricao']

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['matricula','nome','telefone','email']