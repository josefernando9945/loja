
from django.db import models

ESTADO_PAGO = 'Pago'
ESTADO_AGARDANDO_PAGAMENTO = 'Aguardando pagamento'
ESTADO_DEVOLUCAO_DE_PAGAMENTO = 'Devolução do pagamento'
ESTADO_DEVOLUCAO_PARCIAL_DE_PAGAMENTO = 'Devolução parcial do pagamento'


ESTADO_DO_PAGAMENTO = [
    (ESTADO_PAGO, 'Pago'),
    (ESTADO_AGARDANDO_PAGAMENTO, 'Aguardando pagamento'),
    (ESTADO_DEVOLUCAO_DE_PAGAMENTO, 'Devolução do pagamento'),
    (ESTADO_DEVOLUCAO_PARCIAL_DE_PAGAMENTO, 'Devolução parcial do pagamento')
]


class Cliente(models.Model):
    class Meta:
        verbose_name = 'Cliente'

    nome = models.CharField(max_length=255)
    telefone = models.IntegerField()
    email = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nome}'


class Ordem(models.Model):
    class Meta:
        verbose_name = 'Ordem'

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    nome_cliente = models.CharField(max_length=255,null=True, blank=True)
    produto = models.CharField(max_length=255)
    nunero = models.CharField(max_length=50)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50)
    status_pagamento = models.CharField(max_length=255, choices=ESTADO_DO_PAGAMENTO)

    def __str__(self):
        return f'{self.cliente}'



class Item(models.Model):

    class Meta:
        verbose_name = 'Item'

    ordem = models.ForeignKey(Ordem, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    valor_do_item = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.item}'

