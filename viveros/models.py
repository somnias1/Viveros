from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib import auth

class Productor(models.Model):
    cedula = models.PositiveIntegerField(
            primary_key=True,
            )

    nombre_1 = models.CharField(
            max_length=20,
            validators=[MinLengthValidator(3, "El primer nombre debe tener al menos 3 letras")]
            )

    nombre_2 = models.CharField(
            max_length=20,
            blank = True,
            validators=[MinLengthValidator(3, "El segundo nombre debe tener al menos 3 letras")]
            )
    apellido_1 = models.CharField(
            max_length=20,
            validators=[MinLengthValidator(3, "El primer apellido debe tener al menos 3 letras")]
            )

    apellido_2 = models.CharField(
            max_length=20,
            validators=[MinLengthValidator(3, "El segundo apellido debe tener al menos 3 letras")],
            )

    correo = models.EmailField(max_length=254, blank=False, default="correo@ejemplo.com", unique=True)

    def __str__(self):
        return str(self.cedula)

class Vivero(models.Model):
    IdAs = models.CharField(
        validators=[MinLengthValidator(2, "El ID asignado es muy corto"),
        MaxLengthValidator(60,"El ID asignado es muy largo")],
        primary_key=True,
        max_length=60
        )
    nombre_vivero = models.CharField(max_length=60)
    municipio = models.CharField(max_length=40)
    departamento = models.CharField(max_length=40)
    planta = models.CharField(max_length=100)
    productor = models.ForeignKey('Productor', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nombre_vivero

class ProductoControl(models.Model):
    TiposProductos=(
        ('CH','Control Hongo'),
        ('CP','Control Plaga'),
        ('CF','Control Fertilizante')
        )
    ICA = models.CharField(
            primary_key=True,
            max_length=100
            )
    nombre_producto_control = models.CharField(max_length=100)
    frecuencia = models.PositiveIntegerField(help_text="Frecuencia de aplicado en dias")
    valor = models.PositiveIntegerField(help_text="Valor del producto de control")

    def __str__(self):
        return self.nombre_producto_control

class ProductoControlHongo(ProductoControl):
    periodo_de_carencia = models.PositiveIntegerField(help_text="En dias", default=1)
    nombre_hongo_afectado = models.CharField(max_length=100, default="Seta")

    def __str__(self):
        return self.nombre_producto_control

class ProductoControlPlaga(ProductoControl):
    periodo_de_carencia = models.PositiveIntegerField(help_text="En dias", default=1)

    def __str__(self):
        return self.nombre_producto_control

class ProductoControlFertilizante(ProductoControl):
    #periodo_de_carencia = models.PositiveIntegerField(help_text="Si aplica, en dias", blank=True, default=1, null=True)
    def __str__(self):
        return self.nombre_producto_control

class Labor(models.Model):
    descripcion = models.CharField(max_length=1000, help_text="Trabajo realizado")
    fecha = models.DateField(auto_now=True)
    IdAs = models.ForeignKey('Vivero', on_delete=models.CASCADE, null=True)
    producto_hongo = models.ForeignKey('ProductoControlHongo', on_delete=models.RESTRICT, null=True, blank=True)
    producto_plaga = models.ForeignKey('ProductoControlPlaga', on_delete=models.RESTRICT, null=True, blank=True)
    producto_fertilizante = models.ForeignKey('ProductoControlFertilizante', on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return str(self.id)

"""class Empleado(Productor):
    correo2 = models.EmailField(max_length=254, blank=False, default="correo@ejemplo.com", unique=True)

    def __str__(self):
        return str(self.cedula)"""
from django.contrib.auth.models import Group

class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        empleados=Group.objects.get(name='Empleado')
        empleados.user_set.add(self.id)
        return "@{}".format(self.username)


