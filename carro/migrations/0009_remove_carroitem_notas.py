# Generated by Django 4.2.4 on 2023-09-22 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0008_carroitem_variaciones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carroitem',
            name='notas',
        ),
    ]
