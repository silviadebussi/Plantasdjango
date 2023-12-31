# Generated by Django 4.2.6 on 2023-12-06 22:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('Casa', 'Planta de enfeite'), ('Jardim', 'Planta natural')], max_length=100)),
                ('manutencao', models.CharField(max_length=100)),
                ('cultivo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('user', models.OneToOneField(default='padrao', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('PC', 'Pagamento Confirmado'), ('PE', 'Pedido enviado'), ('AG', 'Aguardando Pagamento'), ('PEN', 'Pedido entregue')], default='AG', max_length=3)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preço', models.FloatField()),
                ('descricao', models.CharField(max_length=100)),
                ('cuidados', models.CharField(max_length=100)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagens_plantas/')),
                ('categorias', models.ManyToManyField(related_name='categorias', to='aplic.categorias')),
            ],
            options={
                'verbose_name': 'Planta',
                'verbose_name_plural': 'Plantas',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_pedido', models.CharField(max_length=10, null=True, unique=True)),
                ('status', models.CharField(choices=[('PC', 'Pagamento Confirmado'), ('PE', 'Pedido enviado'), ('AG', 'Aguardando Pagamento'), ('PEN', 'Pedido entregue')], max_length=100)),
                ('data_hora', models.DateField()),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.cliente')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('preço', models.FloatField()),
                ('subtotal', models.DecimalField(decimal_places=2, default=1, max_digits=10, null=True)),
                ('pedido', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.pedido')),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.planta')),
            ],
            options={
                'verbose_name': 'Item de Pedido',
                'verbose_name_plural': 'Itens de Pedido',
            },
        ),
        migrations.CreateModel(
            name='HistoricoStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.pedido')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.status')),
            ],
            options={
                'verbose_name': 'Histórico de Status',
                'verbose_name_plural': 'Históricos de Status',
            },
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_especie', models.CharField(max_length=100)),
                ('descrição', models.CharField(max_length=100)),
                ('Categoria_Botânica', models.CharField(max_length=100)),
                ('Necessidades_de_Luz', models.CharField(max_length=100)),
                ('Usos_da_Espécie', models.CharField(max_length=100)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagens_especies/')),
                ('Planta', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aplic.planta')),
            ],
            options={
                'verbose_name': 'Espécie',
                'verbose_name_plural': 'Espécies',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('complemento', models.IntegerField(default=1)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('SP', 'São Paulo'), ('MA', 'Maranhão'), ('SE', 'Sergipe'), ('CE', 'Ceará'), ('MT', 'Mato Grosso'), ('MG', 'Minas Gerais'), ('RO', 'Rondônia'), ('DF', 'Distrito Federal'), ('GO', 'Goiás'), ('SC', 'Santa Catarina'), ('BA', 'Bahia'), ('AL', 'Alagoas'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('AM', 'Amazonas'), ('RJ', 'Rio de Janeiro'), ('ES', 'Espirito Santo'), ('RN', 'Rio Grande do Norte'), ('TO', 'Tocantins'), ('RR', 'Roraima'), ('PR', 'Paraná'), ('AP', 'Amapá'), ('MS', 'Mato Grosso do Sul'), ('PI', 'Piauí'), ('AC', 'Acre'), ('RS', 'Rio Grande do Sul')], default='MG', max_length=200)),
                ('cep', models.CharField(max_length=100)),
                ('endereco_padrao', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.cliente')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('metodo_pagamento', models.CharField(choices=[('cartao_credito', 'Cartão de crédito'), ('pix', 'PIX')], default='PIX', max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.cliente')),
                ('endereco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.endereco')),
                ('itens', models.ManyToManyField(to='aplic.itempedido')),
            ],
        ),
        migrations.CreateModel(
            name='AvaliacaoCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliacao', models.PositiveIntegerField()),
                ('comentario', models.TextField(blank=True, null=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ManyToManyField(related_name='avaliacoes_categoria', to='aplic.categorias')),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'AvaliacaoCategoria',
                'verbose_name_plural': 'AvaliacoesCategorias',
            },
        ),
    ]
