# Generated by Django 2.1.1 on 2018-10-13 16:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cad_costos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('fecha_trabajo', models.DateField(default=datetime.datetime.now)),
                ('modo_pago_c', models.CharField(choices=[('E', 'Efectivo'), ('T', 'Tarjeta')], max_length=1)),
                ('cantidad_costo', models.DecimalField(decimal_places=2, max_digits=8)),
                ('precio_costo', models.DecimalField(decimal_places=2, max_digits=12)),
                ('valor_costo', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Cad_est_finan',
            fields=[
                ('slug', models.SlugField(unique=True)),
                ('mes_año', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('fec_inicio', models.DateField()),
                ('fec_final', models.DateField()),
                ('ingreso_mes', models.DecimalField(decimal_places=2, max_digits=12)),
                ('ingreso_acum', models.DecimalField(decimal_places=2, max_digits=12)),
                ('costo_tarjeta_mes', models.DecimalField(decimal_places=2, max_digits=12)),
                ('costo_efectivo_mes', models.DecimalField(decimal_places=2, max_digits=12)),
                ('costo_acum', models.DecimalField(decimal_places=2, max_digits=12)),
                ('res_econom_mes', models.DecimalField(decimal_places=2, max_digits=12)),
                ('res_econom_acum', models.DecimalField(decimal_places=2, max_digits=12)),
                ('stock_tarjeta', models.DecimalField(decimal_places=2, max_digits=12)),
                ('stock_efectivo', models.DecimalField(decimal_places=2, max_digits=12)),
                ('saldo_caja_mes', models.DecimalField(decimal_places=2, max_digits=12)),
                ('saldo_caja_acum', models.DecimalField(decimal_places=2, max_digits=12)),
                ('saldo_caja_neto', models.DecimalField(decimal_places=2, max_digits=12)),
                ('res_finan_mes', models.DecimalField(decimal_places=2, max_digits=12)),
                ('res_finan_acum', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Cad_ing_ret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('fecha_trabajo', models.DateField()),
                ('ind_ing_egr', models.CharField(choices=[('I', 'Ingreso'), ('E', 'Egreso')], max_length=1)),
                ('num_veces_i', models.SmallIntegerField()),
                ('valor_ing_ret', models.DecimalField(decimal_places=2, max_digits=12)),
                ('notas', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cad_insumos',
            fields=[
                ('cod_insumo', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('nombre_insumo', models.CharField(max_length=50)),
                ('fecha_cadastro', models.DateField(default=datetime.datetime.now)),
                ('ind_C_V_A', models.CharField(choices=[('C', 'Consumo'), ('V', 'Venta'), ('A', 'Ambos')], max_length=1)),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Cad_stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('fec_movimiento', models.DateField(default=datetime.datetime.now)),
                ('num_veces', models.SmallIntegerField()),
                ('cantidad_mov', models.DecimalField(decimal_places=2, max_digits=8)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=12)),
                ('valor_insumo', models.DecimalField(decimal_places=2, max_digits=12)),
                ('ind_ing_sal', models.CharField(choices=[('I', 'Ingreso'), ('S', 'Salida')], default='I', max_length=1)),
                ('modo_pago_m', models.CharField(choices=[('E', 'Efectivo'), ('T', 'Tarjeta')], default='E', max_length=1)),
                ('cod_insumo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastroCostos.Cad_insumos')),
            ],
        ),
        migrations.CreateModel(
            name='Cad_un_med',
            fields=[
                ('un_med_insumo', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('descripcion', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Cad_V_mesas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('fecha_trabajo', models.DateField(default=datetime.datetime.now)),
                ('num_mesa', models.SmallIntegerField()),
                ('num_veces', models.SmallIntegerField()),
                ('valor_vendido', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='cad_v_mesas',
            unique_together={('fecha_trabajo', 'num_mesa', 'num_veces')},
        ),
        migrations.AddField(
            model_name='cad_insumos',
            name='un_med_insumo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastroCostos.Cad_un_med'),
        ),
        migrations.AlterUniqueTogether(
            name='cad_ing_ret',
            unique_together={('fecha_trabajo', 'ind_ing_egr', 'num_veces_i')},
        ),
        migrations.AddField(
            model_name='cad_costos',
            name='cod_insumo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastroCostos.Cad_insumos'),
        ),
        migrations.AlterUniqueTogether(
            name='cad_stock',
            unique_together={('cod_insumo', 'fec_movimiento', 'num_veces')},
        ),
        migrations.AlterUniqueTogether(
            name='cad_costos',
            unique_together={('fecha_trabajo', 'cod_insumo', 'modo_pago_c')},
        ),
    ]
