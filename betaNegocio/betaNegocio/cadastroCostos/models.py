from django.db import models
from django.db.models import Max
from datetime import datetime
# Create your models here.





class Cad_un_med(models.Model):
    un_med_insumo = models.SmallIntegerField(primary_key= True, null= False, blank= False)
    descripcion = models.CharField(max_length=8)

    def __str__(self):
        return self.descripcion

    def get_nextCodigo(*args ):
        next_codigo = Cad_un_med.objects.all().aggregate(Max('un_med_insumo'))
        print(next_codigo['un_med_insumo__max'])
        if next_codigo['un_med_insumo__max'] == None:
            return 1
        else:
            return next_codigo['un_med_insumo__max'] + 1




class Cad_insumos(models.Model):


    cod_insumo = models.SmallIntegerField(primary_key=True, null=False, blank=False)
    nombre_insumo = models.CharField(max_length=50)
    un_med_insumo = models.ForeignKey(Cad_un_med, null=False, blank=False, on_delete=models.PROTECT)
    fecha_cadastro = models.DateField(default=datetime.now)

    # def __str__(self):
    #     cadena = "{0} -> {1}"
    #     return cadena.format(self.nombre_insumo, self.un_med_insumo)
    def __str__(self):
        return self.nombre_insumo

    def get_nextCodigo(*args):
        next_codigo = Cad_insumos.objects.all().aggregate(Max('cod_insumo'))
        print (next_codigo['cod_insumo__max'])
        if next_codigo['cod_insumo__max'] == None:
            return 1
        else:
            return next_codigo['cod_insumo__max'] + 1
        # return next_codigo['cod_insumo__max'] + 1



class Cad_stock(models.Model):
    cod_insumo = models.ForeignKey(Cad_insumos, null=False, blank=False, on_delete=models.PROTECT)
    fec_movimiento = models.DateField(default=datetime.now)
    num_veces = models.SmallIntegerField()
    cantidad_mov = models.DecimalField(max_digits=8, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=4)
    valor_insumo = models.DecimalField(max_digits=12, decimal_places=4)
    ind_ing_sal_CHOICES = (('I', 'Ingreso'),('S', 'Salida'))
    ind_ing_sal = models.CharField(max_length=1, choices= ind_ing_sal_CHOICES, default = 'I')
    modo_pago_m_CHOICES = (('E', 'Efectivo'), ('T', 'Tarjeta'))
    """CAMBIO A LAS 12:29 PERU 2"""
    """CONFIRMAR SI DEFAULT DE MODO DE PAGO SERA EFECTIVO"""
    modo_pago_m = models.CharField(max_length=1, choices= modo_pago_m_CHOICES, default= 'E')

    def get_numveces_Fecha(fecha,codigo):
        print(fecha)
        print(type(fecha))
        print(codigo)
        print(type(codigo))
        # data =  Cad_stock.objects.filter(fec_movimiento=fecha, cod_insumo=codigo).exists()
        if str(fecha)=="" or str(codigo)=="":
            return 1

        next_numveces = Cad_stock.objects.filter(fec_movimiento=fecha, cod_insumo=codigo).aggregate(Max('num_veces'))

        if next_numveces['num_veces__max'] == None:
            return 1
        else:
            return next_numveces['num_veces__max'] + 1



    class Meta:
        unique_together = ["cod_insumo", "fec_movimiento", "num_veces"]

    # def getnextNum_veces(*args):
    #     print("Reached1")
    #     print(args)
    #     next_num_veces = Cad_stock.objects.filter(cod_insumo=1, fec_movimiento=args)
    #     print(next_num_veces)
    #     print("Reached2")
    #     return "Works"
    #         # next_num_veces['num_veces__max'] + 1



class Cad_ing_ret(models.Model):
    fecha_trabajo = models.DateField()
    ind_ing_egr_CHOICES = (('I', 'Ingreso'), ('E', 'Egreso'))
    ind_ing_egr = models.CharField(max_length=1, choices= ind_ing_egr_CHOICES)
    num_veces_i = models.SmallIntegerField()
    valor_ing_ret = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        unique_together = ["fecha_trabajo", "ind_ing_egr", "num_veces_i"]

class Cad_costos(models.Model):
    fecha_trabajo =  models.DateField(default=datetime.now)
    cod_insumo = models.ForeignKey(Cad_insumos, null=False, blank=False, on_delete=models.CASCADE)
    cantidad_costo = models.DecimalField(max_digits=8, decimal_places=2)
    precio_costo = models.DecimalField(max_digits=12, decimal_places=4)
    valor_costo = models.CharField(max_length=8)
    modo_pago_c_CHOICES = (('E', 'Efectivo'), ('T', 'Tarjeta'))
    modo_pago_c = models.CharField(max_length=1, choices=modo_pago_c_CHOICES)

    class Meta:
        unique_together = ["fecha_trabajo", "cod_insumo"]

class Cad_V_mesas(models.Model):
    fecha_trabajo = models.DateField()
    num_mesa = models.SmallIntegerField()
    num_veces = models.SmallIntegerField()
    valor_vendido = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        unique_together = ["fecha_trabajo", "num_mesa", "num_veces"]

class Cad_est_finan(models.Model):
    mes_año = models.CharField(primary_key=True, max_length=8, null=False, blank=False)
    fec_inicio = models.DateField()
    fec_final = models.DateField()
    tot_ingresos = models.DecimalField(max_digits=12, decimal_places=4)
    tot_costo = models.DecimalField(max_digits=12, decimal_places=4)
    saldo_finan = models.DecimalField(max_digits=12, decimal_places=4)



