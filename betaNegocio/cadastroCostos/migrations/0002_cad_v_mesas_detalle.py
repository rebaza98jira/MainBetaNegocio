# Generated by Django 2.1.1 on 2018-10-13 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastroCostos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cad_V_mesas_detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linea', models.SmallIntegerField()),
                ('cantidad_venta', models.SmallIntegerField()),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=12)),
                ('cabecera', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastroCostos.Cad_V_mesas', to_field='slug')),
                ('cod_insumo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastroCostos.Cad_insumos')),
            ],
        ),
    ]