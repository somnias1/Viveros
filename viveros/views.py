from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from viveros.models import Productor, Vivero, ProductoControl, ProductoControlHongo, ProductoControlPlaga, ProductoControlFertilizante, Labor#, Empleado

# Create your views here.

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        pr = Productor.objects.all().count()
        vi = Vivero.objects.all()
        ctx = {'productor_count': pr, 'vivero_list': vi}
        return render(request, 'viveros/vivero_list.html', ctx)

##########CRUD Productor

class ProductorView(LoginRequiredMixin, View):
    def get(self, request):
        prod = Productor.objects.all()
        ctx = {'productor_list': prod}
        return render(request, 'viveros/productor_list.html', ctx)

class ProductorCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'viveros.add_productor'
    model = Productor
    fields = '__all__'
    success_url = reverse_lazy('viveros:all')


class ProductorUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Productor
    permission_required = 'viveros.change_productor'
    fields = '__all__'
    success_url = reverse_lazy('viveros:all')

class ProductorDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Productor
    permission_required = 'viveros.delete_productor'
    fields = '__all__'
    success_url = reverse_lazy('viveros:all')


##########CRUD Vivero
#@staff_member_required
class ViveroCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'viveros.add_vivero'
    model = Vivero
    fields = '__all__'
    success_url = reverse_lazy('viveros:all')


class ViveroUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'viveros.change_vivero'
    model = Vivero
    fields = '__all__'
    success_url = reverse_lazy('viveros:all')

class ViveroDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Vivero
    permission_required = 'viveros.delete_vivero'
    fields = '__all__'
    success_url = reverse_lazy('viveros:all')

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
    success_url = reverse_lazy('viveros:all')

class ProductoControlUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ProductoControl
    permission_required = 'viveros.change_producto_control'
    fields = '__all__'
    success_url = reverse_lazy('viveros:all')

class ProductoControlDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ProductoControl
    permission_required = 'viveros.delete_producto_control'
    fields = '__all__'
    success_url = reverse_lazy('viveros:all')

##########CRUD Producto Control Hongo

class ProductoControlHongoView(LoginRequiredMixin, View):
    def get(self, request):
        prodctrl = ProductoControlHongo.objects.all()
        ctx = {'productocontrolhongo_list': prodctrl}
        return render(request, 'viveros/productocontrolhongo_list.html', ctx)

class ProductoControlHongoCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ProductoControlHongo
    permission_required = 'viveros.add_productocontrolhongo'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolhongo_list')


class ProductoControlHongoUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ProductoControlHongo
    permission_required = 'viveros.change_productocontrolhongo'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolhongo_list')

class ProductoControlHongoDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ProductoControlHongo
    permission_required = 'viveros.delete_productocontrolhongo'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolhongo_list')

##########CRUD Producto Control Plaga

class ProductoControlPlagaView(LoginRequiredMixin, View):
    def get(self, request):
        prodctrl = ProductoControlPlaga.objects.all()
        ctx = {'productocontrolplaga_list': prodctrl}
        return render(request, 'viveros/productocontrolplaga_list.html', ctx)

class ProductoControlPlagaCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ProductoControlPlaga
    permission_required = 'viveros.add_productocontrolplaga'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolplaga_list')


class ProductoControlPlagaUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ProductoControlPlaga
    permission_required = 'viveros.change_productocontrolplaga'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolplaga_list')

class ProductoControlPlagaDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ProductoControlPlaga
    permission_required = 'viveros.delete_productocontrolplaga'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolplaga_list')

##########CRUD Producto Control Fertilizante

class ProductoControlFertilizanteView(LoginRequiredMixin, View):
    def get(self, request):
        prodctrl = ProductoControlFertilizante.objects.all()
        ctx = {'productocontrolfertilizante_list': prodctrl}
        return render(request, 'viveros/productocontrolfertilizante_list.html', ctx)

class ProductoControlFertilizanteCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = ProductoControlFertilizante
    permission_required = 'viveros.add_productocontrolfertilizante'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolfertilizante_list')


class ProductoControlFertilizanteUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ProductoControlFertilizante
    permission_required = 'viveros.change_productocontrolfertilizante'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolfertilizante_list')

class ProductoControlFertilizanteDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ProductoControlFertilizante
    permission_required = 'viveros.delete_productocontrolfertilizante'
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolfertilizante_list')

##########CRUD Labor
class LaborView(LoginRequiredMixin, View):
    def get(self, request):
        lab = Labor.objects.all()
        ctx = {'labor_list': lab}
        return render(request, 'viveros/labor_list.html', ctx)

class LaborCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Labor
    permission_required = 'viveros.add_labor'
    fields = '__all__'
    success_url = reverse_lazy('viveros:labor_list')

class LaborUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Labor
    permission_required = 'viveros.change_labor'
    fields = '__all__'
    success_url = reverse_lazy('viveros:labor_list')

class LaborDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Labor
    permission_required = 'viveros.delete_labor'
    fields = '__all__'
    success_url = reverse_lazy('viveros:labor_list')

##########Registro
"""
class EmpleadoCreate(LoginRequiredMixin, CreateView):
    model = Empleado
    fields = '__all__'
    success_url = reverse_lazy('viveros:labor_list')"""

from django.urls import reverse_lazy
from . import forms

class SignUp(CreateView, PermissionRequiredMixin):
    permission_required = 'auth.add_user'
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('viveros:all')
    template_name = 'accounts/signup.html'


