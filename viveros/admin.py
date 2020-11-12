from django.contrib import admin

# Register your models here.

from viveros.models import Productor, Vivero, ProductoControl, ProductoControlHongo, ProductoControlPlaga, ProductoControlFertilizante, Labor

admin.site.register(Productor)
admin.site.register(Vivero)
admin.site.register(ProductoControl)
admin.site.register(ProductoControlHongo)
admin.site.register(ProductoControlPlaga)
admin.site.register(ProductoControlFertilizante)
admin.site.register(Labor)