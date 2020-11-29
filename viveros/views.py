from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from viveros.models import Productor, Vivero, ProductoControl, ProductoControlHongo, ProductoControlPlaga, ProductoControlFertilizante, Labor#, Empleado
from django.db.models import Q
from ads.utils import dump_queries
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
import csv
from django.http import HttpResponse

# Create your views here.

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        pr = Productor.objects.all().count()
        vi = Vivero.objects.all()
        ctx = {'productor_count': pr, 'vivero_list': vi}
        return render(request, 'viveros/vivero_list.html', ctx)

##########CRUD Productor
def exporte_productores_csv(query):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="productores.csv"'
    writer = csv.writer(response)
    writer.writerow(['Cedula', 'Nombre 1', 'Nombre 2', 'Apellido 1', 'Apellido 2', 'Correo'])
    prl = Productor.objects.filter(query).select_related().values_list('cedula', 'nombre_1', 'nombre_2', 'apellido_1', 'apellido_2', 'correo')
    for pr in prl:
        writer.writerow(pr)

    return response

class ProductorView(LoginRequiredMixin, View):
    model = Productor
    template_name = "viveros/productor_list.html"

    def get(self, request) :
        strval =  request.GET.get("search", False)

        if strval :
            query = Q(cedula__icontains=strval) | Q(nombre_1__icontains=strval) | Q(nombre_2__icontains=strval) | Q(apellido_1__icontains=strval) | Q(apellido_2__icontains=strval) | Q(correo__icontains=strval)
            productor_list = Productor.objects.filter(query).select_related()#.values_list()
            #resp = exporte_productores_csv(query)
        else:
            productor_list = Productor.objects.all()
        ctx = {'productor_list' : productor_list}
        retval=render(request, self.template_name, ctx)
        dump_queries()
        return  retval#resp

class ProductorCreate(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'viveros.add_productor'
    model = Productor
    fields = '__all__'
    success_url = reverse_lazy('viveros:productor_list')
    success_message = 'Productor creado correctamente'


class ProductorUpdate(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Productor
    permission_required = 'viveros.change_productor'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productor_list')
    success_message = 'Productor actualizado correctamente'

class ProductorDelete(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Productor
    permission_required = 'viveros.delete_productor'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productor_list')
    success_message = 'Productor eliminado correctamente'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ProductorDelete, self).delete(request, *args, **kwargs)

class ProductorDetail(DetailView, LoginRequiredMixin):
    template_name = 'viveros/productor_detail.html'
    model = Productor


##########CRUD Vivero
#@staff_member_required

class ViveroView(LoginRequiredMixin, View):
    model = Vivero
    template_name = "viveros/vivero_list.html"

    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            query = Q(IdAs__icontains=strval) | Q(nombre_vivero__icontains=strval) | Q(municipio__icontains=strval) | Q(departamento__icontains=strval) | Q(planta__icontains=strval) | Q(productor__nombre_1__icontains=strval) | Q(productor__nombre_2__icontains=strval) | Q(productor__apellido_1__icontains=strval) | Q(productor__apellido_2__icontains=strval) | Q(productor__correo__icontains=strval)
            vivero_list = Vivero.objects.filter(query).select_related()
        else:
            vivero_list = Vivero.objects.all()

        ctx = {'vivero_list' : vivero_list}
        retval=render(request, self.template_name, ctx)
        dump_queries()
        return retval;

class ViveroCreate(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'viveros.add_vivero'
    model = Vivero
    fields = '__all__'
    success_url = reverse_lazy('viveros:vivero_list')
    success_message = 'Vivero creado correctamente'


class ViveroUpdate(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'viveros.change_vivero'
    model = Vivero
    fields = '__all__'
    success_url = reverse_lazy('viveros:vivero_list')
    success_message = 'Vivero actualizado correctamente'

class ViveroDelete(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Vivero
    permission_required = 'viveros.delete_vivero'
    fields = '__all__'
    success_url = reverse_lazy('viveros:vivero_list')
    success_message = 'Vivero eliminado correctamente'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ViveroDelete, self).delete(request, *args, **kwargs)

class ViveroDetail(DetailView, LoginRequiredMixin):
    template_name = 'viveros/vivero_detail.html'
    model = Vivero


##########CRUD Producto Control

class ProductoControlView(LoginRequiredMixin, View):
    def get(self, request):
        prodctrl = ProductoControl.objects.all()
        ctx = {'productocontrol_list': prodctrl}
        return render(request, 'viveros/productocontrol_list.html', ctx)

class ProductoControlCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ProductoControl
    permission_required = 'viveros.add_producto_control'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrol_list')

class ProductoControlUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ProductoControl
    permission_required = 'viveros.change_producto_control'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrol_list')

class ProductoControlDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ProductoControl
    permission_required = 'viveros.delete_producto_control'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrol_list')


##########CRUD Producto Control Hongo

class ProductoControlHongoView(LoginRequiredMixin, View):
    model = ProductoControlHongo
    template_name = "viveros/productocontrolhongo_list.html"

    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            query = Q(nombre_producto_control__icontains=strval) | Q(ICA__icontains=strval) | Q(nombre_hongo_afectado__icontains=strval)
            productocontrolhongo_list = ProductoControlHongo.objects.filter(query).select_related()
        else:
            productocontrolhongo_list = ProductoControlHongo.objects.all()

        ctx = {'productocontrolhongo_list' : productocontrolhongo_list}
        retval=render(request, self.template_name, ctx)
        dump_queries()
        return retval;

class ProductoControlHongoCreate(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ProductoControlHongo
    permission_required = 'viveros.add_productocontrolhongo'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolhongo_list')
    success_message = 'Producto de control de hongos creado correctamente'


class ProductoControlHongoUpdate(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ProductoControlHongo
    permission_required = 'viveros.change_productocontrolhongo'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolhongo_list')
    success_message = 'Producto de control de hongos actualizado correctamente'

class ProductoControlHongoDelete(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ProductoControlHongo
    permission_required = 'viveros.delete_productocontrolhongo'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolhongo_list')
    success_message = 'Producto de control de hongos borrado correctamente'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ProductoControlHongoDelete, self).delete(request, *args, **kwargs)

class ProductoControlHongoDetail(DetailView, LoginRequiredMixin):
    template_name = 'viveros/productocontrolhongo_detail.html'
    model = ProductoControlHongo

##########CRUD Producto Control Plaga

class ProductoControlPlagaView(LoginRequiredMixin, View):
    model = ProductoControlPlaga
    template_name = "viveros/productocontrolplaga_list.html"

    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            query = Q(nombre_producto_control__icontains=strval) | Q(ICA__icontains=strval)
            productocontrolplaga_list = ProductoControlPlaga.objects.filter(query).select_related()
        else:
            productocontrolplaga_list = ProductoControlPlaga.objects.all()

        ctx = {'productocontrolplaga_list' : productocontrolplaga_list}
        retval=render(request, self.template_name, ctx)
        dump_queries()
        return retval;

class ProductoControlPlagaCreate(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ProductoControlPlaga
    permission_required = 'viveros.add_productocontrolplaga'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolplaga_list')
    success_message = 'Producto de control de plagas creado correctamente'


class ProductoControlPlagaUpdate(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ProductoControlPlaga
    permission_required = 'viveros.change_productocontrolplaga'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolplaga_list')
    success_message = 'Producto de control de plagas actualizado correctamente'

class ProductoControlPlagaDelete(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ProductoControlPlaga
    permission_required = 'viveros.delete_productocontrolplaga'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolplaga_list')
    success_message = 'Producto de control de plagas eliminado correctamente'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ProductoControlPlagaDelete, self).delete(request, *args, **kwargs)

class ProductoControlPlagaDetail(DetailView, LoginRequiredMixin):
    template_name = 'viveros/productocontrolplaga_detail.html'
    model = ProductoControlPlaga

##########CRUD Producto Control Fertilizante

class ProductoControlFertilizanteView(LoginRequiredMixin, View):
    model = ProductoControlFertilizante
    template_name = "viveros/productocontrolfertilizante_list.html"

    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            query = Q(nombre_producto_control__icontains=strval) | Q(ICA__icontains=strval)
            productocontrolfertilizante_list = ProductoControlFertilizante.objects.filter(query).select_related()
        else:
            productocontrolfertilizante_list = ProductoControlFertilizante.objects.all()

        ctx = {'productocontrolfertilizante_list' : productocontrolfertilizante_list}
        retval=render(request, self.template_name, ctx)
        dump_queries()
        return retval;

class ProductoControlFertilizanteCreate(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ProductoControlFertilizante
    permission_required = 'viveros.add_productocontrolfertilizante'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolfertilizante_list')
    success_message = 'Producto de control fertilizante creado correctamente'

class ProductoControlFertilizanteUpdate(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ProductoControlFertilizante
    permission_required = 'viveros.change_productocontrolfertilizante'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolfertilizante_list')
    success_message = 'Producto de control fertilizante actualizado correctamente'

class ProductoControlFertilizanteDelete(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ProductoControlFertilizante
    permission_required = 'viveros.delete_productocontrolfertilizante'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolfertilizante_list')
    success_message = 'Producto de control fertilizante eliminado correctamente'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ProductoControlFertilizanteDelete, self).delete(request, *args, **kwargs)

class ProductoControlFertilizanteDetail(DetailView, LoginRequiredMixin):
    template_name = 'viveros/productocontrolfertilizante_detail.html'
    model = ProductoControlFertilizante

##########CRUD Labor
class LaborView(LoginRequiredMixin, View):
    model = Labor
    template_name = "viveros/labor_list.html"

    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            query = Q(IdAs__nombre_vivero__icontains=strval) | Q(producto_hongo__nombre_producto_control__icontains=strval) | Q(producto_plaga__nombre_producto_control__icontains=strval) | Q(producto_fertilizante__nombre_producto_control__icontains=strval)
            labor_list = Labor.objects.filter(query).select_related()
        else:
            labor_list = Labor.objects.all()#.order_by('-fecha')[:10]

        ctx = {'labor_list' : labor_list}
        retval=render(request, self.template_name, ctx)
        dump_queries()
        return retval;

class LaborCreate(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Labor
    permission_required = 'viveros.add_labor'
    fields = '__all__'
    success_url = reverse_lazy('viveros:labor_list')
    success_message = 'Labor creada correctamente'

class LaborUpdate(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Labor
    permission_required = 'viveros.change_labor'
    fields = '__all__'
    success_url = reverse_lazy('viveros:labor_list')
    success_message = 'Labor actualizada correctamente'

class LaborDelete(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Labor
    permission_required = 'viveros.delete_labor'
    fields = '__all__'
    success_url = reverse_lazy('viveros:labor_list')
    success_message = 'Labor borrada correctamente'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(LaborDelete, self).delete(request, *args, **kwargs)

class LaborDetail(DetailView, LoginRequiredMixin):
    template_name = 'viveros/labor_detail.html'
    model = Labor

##########Registro

from django.urls import reverse_lazy
from . import forms

class SignUp(CreateView, PermissionRequiredMixin):
    permission_required = 'viveros.delete_labor'
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('viveros:vivero_list')
    template_name = 'accounts/signup.html'


