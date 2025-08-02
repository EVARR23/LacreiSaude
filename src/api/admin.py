
from django.contrib import admin
from .models import Profissional, Consulta



@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_social', 'profissional', 'endereco', 'contato')

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'profissional')
  
    
