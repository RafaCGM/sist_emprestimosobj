from django.forms import ModelForm
from .models import Usuario
from .models import Categoria
from django.contrib.auth.forms import UserCreationForm

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome','descricao']

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['matricula','nome','telefone','email']