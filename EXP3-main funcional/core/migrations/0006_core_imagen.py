from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_carrito_remove_producto_cantidad_carritoitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='Jardineria',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='Imagen'),
        ),
    ]
