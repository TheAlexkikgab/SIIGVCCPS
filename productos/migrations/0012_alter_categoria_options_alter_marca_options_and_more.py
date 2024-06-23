# Generated by Django 5.0.6 on 2024-06-23 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0011_alter_producto_id_marca'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='marca',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['nombre']},
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='id_categoria',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='id_marca',
            new_name='marca',
        ),
    ]
