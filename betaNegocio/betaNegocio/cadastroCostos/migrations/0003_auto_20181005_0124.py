# Generated by Django 2.1.1 on 2018-10-05 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastroCostos', '0002_auto_20181004_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cad_costos',
            name='valor_costo',
            field=models.DecimalField(decimal_places=4, max_digits=12),
        ),
    ]