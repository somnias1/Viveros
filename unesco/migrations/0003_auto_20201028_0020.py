# Generated by Django 3.1 on 2020-10-28 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0002_auto_20201028_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]
