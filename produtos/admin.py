import nome as nome
from django.contrib import admin
from .models import *




class TabelaProdutos(admin.TabularInline):
    model = Variante




class MostraProduto(admin.ModelAdmin):
    model = Produtos

    inlines = [TabelaProdutos]

admin.site.register(Produtos, MostraProduto)
admin.site.register(Variante)
