# Generated by Django 3.1 on 2020-10-22 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viveros', '0005_remove_productocontrol_periodo_de_carencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productocontrol',
            name='fecha_aplicado',
        ),
    ]