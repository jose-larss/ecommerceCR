# Generated by Django 4.2.4 on 2023-09-21 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0011_alter_producto_update_defaults'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='update_defaults',
            field=models.BooleanField(default=False),
        ),
    ]
