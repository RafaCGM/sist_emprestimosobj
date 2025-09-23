from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

class RegistroForm(UserCreationForm):
    matricula = forms.CharField(
        max_length=20, 
        label="Matrícula",
        widget=forms.TextInput(attrs={'type': 'text'})
    )

    nome = forms.CharField(max_length=300, label="Nome")
    telefone = forms.CharField(max_length=12, label="Telefone")
    email = forms.EmailField(max_length=200, label="E-mail")

    class Meta:
        model = Usuario
        fields = ['matricula','nome','username','telefone','email']

    def clean_matricula(self):
        matricula = self.cleaned_data['matricula']
        if not matricula.isdigit():
            raise forms.ValidationError("A matrícula deve conter apenas números.")
        return matricula

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome','descricao']

class ObjetoForm(ModelForm):
    class Meta:
        model = Objeto
        fields = ['nome','descricao','categoria']

class EmprestimoForm(ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['usuario','objeto','dataDevolucao']

    dataDevolucao = forms.DateTimeField(required=False) 

class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['usuario', 'objeto', 'dataReserva', 'dataAtendimento']

