from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Cad_un_med, Cad_insumos, Cad_stock, Cad_costos
from django.db.models import Sum, F, ExpressionWrapper, Max
from .forms import Cad_un_med_Form, Cad_insumos_Form, Cad_stock_Form, Cad_stock_insumo_Form, Cad_costos_Form
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from decimal import Decimal

# Create your views here.

def index(request):
  #  return HttpResponse("Index")
    return render(request, 'cadastroCostos/index.html')


class Cad_un_med_List(ListView):
    model = Cad_un_med
    template_name = 'cadastroCostos/cad_un_med_List.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query :
            context = Cad_un_med.objects.filter(descripcion__icontains=query)
            return context
        else:
            return Cad_un_med.objects.all().order_by('un_med_insumo')

class Cad_un_med_Create(CreateView):
    model = Cad_un_med
    form_class = Cad_un_med_Form
    template_name = 'cadastroCostos/cad_un_med_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_un_med_listar')








class Cad_un_med_Detail(DetailView, UpdateView):
    model = Cad_un_med
    form_class = Cad_un_med_Form
    template_name = 'cadastroCostos/cad_un_med_Detail.html'

class Cad_un_med_Update(UpdateView):
    model = Cad_un_med
    form_class = Cad_un_med_Form
    template_name = 'cadastroCostos/cad_un_med_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_un_med_listar')

class Cad_un_med_Delete(DeleteView):
    model = Cad_un_med
    template_name = 'cadastroCostos/cad_un_med_Delete.html'
    success_url = reverse_lazy('betaNegocio:cad_un_med_listar')


class Cad_insumos_List(ListView):
    model = Cad_insumos
    template_name = 'cadastroCostos/cad_insumos_List.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query :
            context = Cad_insumos.objects.filter(nombre_insumo__icontains=query)
            return context
        else:
            return Cad_insumos.objects.all().order_by('cod_insumo')

class Cad_insumos_Create(CreateView):
    model = Cad_insumos
    form_class = Cad_insumos_Form
    template_name = 'cadastroCostos/cad_insumos_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_insumos_listar')

class Cad_insumos_Detail(DetailView, UpdateView):
    model = Cad_insumos
    form_class = Cad_insumos_Form
    template_name = 'cadastroCostos/cad_insumos_Detail.html'

class Cad_insumos_Update(UpdateView):
    model = Cad_insumos
    form_class = Cad_insumos_Form
    template_name = 'cadastroCostos/cad_insumos_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_insumos_listar')

class Cad_insumos_Delete(DeleteView):
    model = Cad_insumos
    template_name = 'cadastroCostos/cad_insumos_Delete.html'
    success_url = reverse_lazy('betaNegocio:cad_insumos_listar')


class Cad_stock_List(ListView,UpdateView):
    model = Cad_stock
    template_name = 'cadastroCostos/cad_stock_List.html'
    paginate_by = 10
    form_class = Cad_stock_insumo_Form

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        # Explicitly states what get to call:
        return ListView.get(self, request, *args, **kwargs)

    def get_queryset(self):
        query = self.request.GET.get("cod_insumo")
        context = Cad_stock.objects.all().order_by('fec_movimiento')

        if query:

            if query.isdigit():
                context = context.filter(cod_insumo=query)
            else:
                context2 = Cad_insumos.objects.filter(nombre_insumo__icontains=query).values_list('cod_insumo',flat=True)
                context = context.filter(cod_insumo__in=context2)
            # return context
        # else:
        #     context = Cad_stock.objects.all()

        return context





class Cad_stock_Create(CreateView):
    model = Cad_stock
    form_class = Cad_stock_Form
    template_name = 'cadastroCostos/cad_stock_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_stock_listar')


class Cad_stock_Detail(DetailView,UpdateView):
    model = Cad_stock
    form_class = Cad_stock_insumo_Form
    template_name = 'cadastroCostos/cad_stock_Detail.html'

    """SLUG PRUEBA"""



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        cadinsumo_value = Cad_stock.objects.only('cod_insumo').get(pk=self.kwargs['pk']).cod_insumo
        context['mov_insumos'] = Cad_stock.objects.all().filter(cod_insumo=cadinsumo_value)
        # context['saldo'] = cantidad_mov_ingresos_suma['cantidad_mov__sum'] - cantidad_mov_salida_suma['cantidad_mov__sum']
        # print (context)
        return context

class Cad_stock_Detail_Movimiento(DetailView, UpdateView):
    model = Cad_stock
    form_class = Cad_stock_Form
    template_name = 'cadastroCostos/cad_stock_detalle_insumo_Detail.html'

class Cad_Stock_Update(UpdateView):
    model = Cad_stock
    form_class = Cad_stock_Form
    template_name = 'cadastroCostos/cad_stock_Form_Editar.html'
    success_url = reverse_lazy('betaNegocio:cad_stock_listar')

class Cad_stock_Delete(DeleteView):
    model = Cad_stock
    template_name = 'cadastroCostos/cad_stock_Delete.html'
    success_url = reverse_lazy('betaNegocio:cad_stock_listar')



class Cad_costos_List(ListView):
    model = Cad_costos
    template_name = 'cadastroCostos/cad_costos_List.html'
    paginate_by = 10

class Cad_costos_Create(CreateView,UpdateView):
    model = Cad_stock
    second_model = Cad_costos
    form_class = Cad_costos_Form
    second_form_class = Cad_stock_Form
    template_name = 'cadastroCostos/cad_costos_Form.html'
    success_url = reverse_lazy('betaNegocio:cad_stock_listar')

    def get_context_data(self, **kwargs):
        context = super(Cad_costos_Create, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        stock = self.model.objects.get(id=pk)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance= stock)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_stock = kwargs['pk']

        stock = self.model.objects.get(id=id_stock)

        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST, instance=stock)
        print("THIS IS AHONTER DEBUGGGGGGGGG")
        print(form2)

        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())



def valida_siguente_vez_fecha(request):
    fec_movimiento = request.GET.get('fec_movimiento', None)
    cod_insumo = request.GET.get('cod_insumo', None)
    print ("DEBUG AJAXEC")
    print(fec_movimiento)
    print(cod_insumo)

    data = {
        'numveces': Cad_stock.get_numveces_Fecha(fec_movimiento,cod_insumo)
    }
    print("DEBUG AJAXDATA")
    print (data)
    return JsonResponse(data)
