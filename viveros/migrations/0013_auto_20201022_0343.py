# Generated by Django 3.1 on 2020-10-22 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viveros', '0012_auto_20201022_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productocontrol',
            name='nombre_hongo_afectado',
            field=models.CharField(blank=True, default='Seta', help_text='Si aplica', max_length=100, null=True),
        ),
    ]