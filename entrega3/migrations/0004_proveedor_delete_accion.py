# Generated by Django 4.1.7 on 2023-04-02 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrega3', '0003_alter_articulo_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=100)),
                ('razon_social', models.TextField(max_length=100)),
                ('rubro', models.TextField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Accion',
        ),
    ]
