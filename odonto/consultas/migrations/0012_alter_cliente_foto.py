# Generated by Django 5.1.7 on 2025-03-24 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0011_alter_cliente_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(default='user.jpg', upload_to='consultas/static/images/'),
        ),
    ]
