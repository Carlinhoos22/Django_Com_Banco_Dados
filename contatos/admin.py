from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao',
    'categoria')
    list_display_links = ('nome', 'sobrenome', 'telefone', 'email')
    list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone', 'email')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
