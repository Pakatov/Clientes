# Generated by Django 5.1.7 on 2025-03-23 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0004_alter_cliente_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='foto',
            field=models.FileField(upload_to=''),
        ),
    ]
