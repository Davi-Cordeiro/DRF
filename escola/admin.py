from django.contrib import admin
from escola.models import Estudante, Curso, Matricula

@admin.register(Estudante)
class Estudantes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'emails', 'cpf', 'data_nascimento', 'celular',)
    list_display_links = ('id', 'nome',)
    list_per_page = 20
    search_fields = ('nome',)

@admin.register(Curso)
class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao',)
    list_display_links = ('id', 'codigo',)
    search_fields = ('codigo',)

@admin.register(Matricula)
class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'periodo', 'estudante')