# Generated by Django 4.2.4 on 2023-09-21 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0009_alter_variacion_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='update_defaults',
            field=models.BooleanField(default=False),
        ),
    ]
