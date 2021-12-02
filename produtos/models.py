from django.db import models

class Produtos(models.Model):
    SLUGIFY_FIELD = 'title'

    class Meta:
        verbose_name = 'Produto'

    nome = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    colecao = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nome}'



class Variante(models.Model):
    class Meta:
        verbose_name = 'Variante'

    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, null=True, blank=True)
    preco_de_custo = models.DecimalField(max_digits=6, decimal_places=2)
    preco_de_venda = models.DecimalField(max_digits=6, decimal_places=2)
    porcentagem = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade = models.IntegerField()
    cor = models.CharField(max_length=50)
    tamanho = models.CharField(max_length=50)
