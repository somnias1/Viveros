# Generated by Django 3.1 on 2020-10-28 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0004_auto_20201028_0021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='states',
            old_name='state',
            new_name='states',
        ),
    ]
