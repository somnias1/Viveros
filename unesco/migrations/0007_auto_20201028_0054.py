# Generated by Django 3.1 on 2020-10-28 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0006_auto_20201028_0037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
    ]
