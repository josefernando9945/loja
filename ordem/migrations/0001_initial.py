# Generated by Django 3.2.9 on 2021-12-02 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.IntegerField()),
                ('email', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='Ordem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=255)),
                ('produto', models.CharField(max_length=255)),
                ('nunero', models.CharField(max_length=50)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_update', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=50)),
                ('status_pagamento', models.CharField(choices=[('Pago', 'Pago'), ('Aguardando pagamento', 'Aguardando pagamento'), ('Devolução do pagamento', 'Devolução do pagamento'), ('Devolução parcial do pagamento', 'Devolução parcial do pagamento')], max_length=255)),
                ('ordem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ordem.cliente')),
            ],
            options={
                'verbose_name': 'Ordem',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('quantidade', models.IntegerField()),
                ('valor_do_item', models.DecimalField(decimal_places=2, max_digits=6)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ordem.cliente')),
            ],
            options={
                'verbose_name': 'Item',
            },
        ),
    ]
