from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from viveros.models import Productor, Vivero, ProductoControl, ProductoControlHongo, ProductoControlPlaga, ProductoControlFertilizante, Labor, Empleado

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

class ProductorCreate(LoginRequiredMixin, CreateView):
    model = Productor
    fields = '__all__'
    success_url = reverse_lazy('viveros:all')


class ProductorUpdate(LoginRequiredMixin, UpdateView):
    model = Productor
    fields = '__all__'
    success_url = reverse_lazy('viveros:all')


class ProductorDelete(LoginRequiredMixin, DeleteView):
    model = Productor
    fields = '__all__'
    success_url = reverse_lazy('viveros:all')


##########CRUD Vivero

class ViveroCreate(LoginRequiredMixin, CreateView):
    model = Vivero
    fields = '__all__'
    success_url = reverse_lazy('viveros:all')


class ViveroUpdate(LoginRequiredMixin, UpdateView):
    model = Vivero
    fields = '__all__'
    success_url = reverse_lazy('viveros:all')


class ViveroDelete(LoginRequiredMixin, DeleteView):
    model = Vivero
    fields = '__all__'
    success_url = reverse_lazy('viveros:all')

##########CRUD Producto Control

class ProductoControlView(LoginRequiredMixin, View):
    def get(self, request):
        prodctrl = ProductoControl.objects.all()
        ctx = {'productocontrol_list': prodctrl}
        return render(request, 'viveros/productocontrol_list.html', ctx)

class ProductoControlCreate(LoginRequiredMixin, CreateView):
    model = ProductoControl
    fields = '__all__'
    success_url = reverse_lazy('viveros:all')


class ProductoControlUpdate(LoginRequiredMixin, UpdateView):
    model = ProductoControl
    fields = '__all__'
    success_url = reverse_lazy('viveros:all')


class ProductoControlDelete(LoginRequiredMixin, DeleteView):
    model = ProductoControl
    fields = '__all__'
    success_url = reverse_lazy('viveros:all')

##########CRUD Producto Control Hongo

class ProductoControlHongoView(LoginRequiredMixin, View):
    def get(self, request):
        prodctrl = ProductoControlHongo.objects.all()
        ctx = {'productocontrolhongo_list': prodctrl}
        return render(request, 'viveros/productocontrolhongo_list.html', ctx)

class ProductoControlHongoCreate(LoginRequiredMixin, CreateView):
    model = ProductoControlHongo
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolhongo_list')


class ProductoControlHongoUpdate(LoginRequiredMixin, UpdateView):
    model = ProductoControlHongo
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolhongo_list')


class ProductoControlHongoDelete(LoginRequiredMixin, DeleteView):
    model = ProductoControlHongo
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolhongo_list')

##########CRUD Producto Control Plaga

class ProductoControlPlagaView(LoginRequiredMixin, View):
    def get(self, request):
        prodctrl = ProductoControlPlaga.objects.all()
        ctx = {'productocontrolplaga_list': prodctrl}
        return render(request, 'viveros/productocontrolplaga_list.html', ctx)

class ProductoControlPlagaCreate(LoginRequiredMixin, CreateView):
    model = ProductoControlPlaga
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolplaga_list')


class ProductoControlPlagaUpdate(LoginRequiredMixin, UpdateView):
    model = ProductoControlPlaga
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolplaga_list')


class ProductoControlPlagaDelete(LoginRequiredMixin, DeleteView):
    model = ProductoControlPlaga
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolplaga_list')

##########CRUD Producto Control Fertilizante

class ProductoControlFertilizanteView(LoginRequiredMixin, View):
    def get(self, request):
        prodctrl = ProductoControlFertilizante.objects.all()
        ctx = {'productocontrolfertilizante_list': prodctrl}
        return render(request, 'viveros/productocontrolfertilizante_list.html', ctx)

class ProductoControlFertilizanteCreate(LoginRequiredMixin, CreateView):
    model = ProductoControlFertilizante
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolfertilizante_list')


class ProductoControlFertilizanteUpdate(LoginRequiredMixin, UpdateView):
    model = ProductoControlFertilizante
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolfertilizante_list')


class ProductoControlFertilizanteDelete(LoginRequiredMixin, DeleteView):
    model = ProductoControlFertilizante
    fields = '__all__'
    success_url = reverse_lazy('viveros:productocontrolfertilizante_list')

##########CRUD Labor
class LaborView(LoginRequiredMixin, View):
    def get(self, request):
        lab = Labor.objects.all()
        ctx = {'labor_list': lab}
        return render(request, 'viveros/labor_list.html', ctx)

class LaborCreate(LoginRequiredMixin, CreateView):
    model = Labor
    fields = '__all__'
    success_url = reverse_lazy('viveros:labor_list')


class LaborUpdate(LoginRequiredMixin, UpdateView):
    model = Labor
    fields = '__all__'
    success_url = reverse_lazy('viveros:labor_list')


class LaborDelete(LoginRequiredMixin, DeleteView):
    model = Labor
    fields = '__all__'
    success_url = reverse_lazy('viveros:labor_list')

##########Registro

class EmpleadoCreate(LoginRequiredMixin, CreateView):
    model = Empleado
    fields = '__all__'
    success_url = reverse_lazy('viveros:labor_list')

from django.urls import reverse_lazy
from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('viveros:all')
    template_name = 'accounts/signup.html'


