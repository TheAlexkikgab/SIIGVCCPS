# Generated by Django 5.0.6 on 2024-06-23 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_alter_producto_caducidad_alter_producto_descripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='marca',
        ),
        migrations.AddField(
            model_name='producto',
            name='id_marca',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='productos.marca'),
        ),
    ]
