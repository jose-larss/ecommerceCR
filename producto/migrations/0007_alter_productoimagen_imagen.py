# Generated by Django 4.2.4 on 2023-09-09 18:16

from django.db import migrations, models
import producto.models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0006_alter_categoria_options_alter_producto_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoimagen',
            name='imagen',
            field=models.ImageField(upload_to=producto.models.comercio_directorio_fotos),
        ),
    ]
