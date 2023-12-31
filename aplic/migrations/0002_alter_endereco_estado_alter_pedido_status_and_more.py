# Generated by Django 4.2.6 on 2023-12-06 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='estado',
            field=models.CharField(choices=[('RJ', 'Rio de Janeiro'), ('MA', 'Maranhão'), ('ES', 'Espirito Santo'), ('MG', 'Minas Gerais'), ('AC', 'Acre'), ('SP', 'São Paulo'), ('RS', 'Rio Grande do Sul'), ('BA', 'Bahia'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('TO', 'Tocantins'), ('MS', 'Mato Grosso do Sul'), ('AP', 'Amapá'), ('SE', 'Sergipe'), ('RN', 'Rio Grande do Norte'), ('GO', 'Goiás'), ('DF', 'Distrito Federal'), ('SC', 'Santa Catarina'), ('PR', 'Paraná'), ('MT', 'Mato Grosso'), ('AL', 'Alagoas'), ('RR', 'Roraima'), ('AM', 'Amazonas'), ('PB', 'Paraíba'), ('RO', 'Rondônia'), ('CE', 'Ceará')], default='MG', max_length=200),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('PC', 'Pagamento Confirmado'), ('PEN', 'Pedido entregue'), ('AG', 'Aguardando Pagamento'), ('PE', 'Pedido enviado')], max_length=100),
        ),
        migrations.AlterField(
            model_name='status',
            name='nome',
            field=models.CharField(choices=[('PC', 'Pagamento Confirmado'), ('PEN', 'Pedido entregue'), ('AG', 'Aguardando Pagamento'), ('PE', 'Pedido enviado')], default='AG', max_length=3),
        ),
    ]
