# Generated by Django 4.1.2 on 2023-06-14 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_producto_cantidad_carrito'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='cantidad_carrito',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='cantidad_disponible',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='fecha_creacion',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='oferta_actual',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='oferta_anterior',
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
