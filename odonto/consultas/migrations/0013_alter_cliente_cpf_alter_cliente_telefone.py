# Generated by Django 5.1.7 on 2025-03-24 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0012_alter_cliente_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=16),
        ),
    ]
