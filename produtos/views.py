from django.shortcuts import render
from django.views.generic import ListView
from produtos.models import Produtos


class ControleProdutos(ListView):
    model = Produtos
    pass