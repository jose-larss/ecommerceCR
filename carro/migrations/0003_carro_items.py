# Generated by Django 4.2.4 on 2023-09-14 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0002_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, to='carro.cartitem'),
        ),
    ]
