from django.contrib import admin
from .models import Usuario, Categoria, Objeto, Emprestimo, Reserva

@admin.register(Usuario)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['nome','matricula']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Objeto)
class ObjetoAdmin(admin.ModelAdmin):
    list_display = ['nome','categoria']

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ['usuario','objeto','dataDevolucao']

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['usuario','objeto','dataReserva']