# Generated by Django 5.1.7 on 2025-03-23 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0005_alter_cliente_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(upload_to=''),
        ),
    ]
