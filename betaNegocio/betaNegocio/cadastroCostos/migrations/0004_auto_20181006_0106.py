# Generated by Django 2.1.1 on 2018-10-06 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastroCostos', '0003_auto_20181005_0124'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='cad_un_med',
            index=models.Index(fields=['un_med_insumo'], name='un_med_insumo_idx'),
        ),
    ]