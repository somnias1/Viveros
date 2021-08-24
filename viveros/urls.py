from django.urls import path
from . import views
#from django.views.generic import TemplateView


app_name = 'viveros'
urlpatterns = [
    #Vivero
    path('vivero/', views.ViveroView.as_view(), name='vivero_list'),
    path('vivero/create/', views.ViveroCreate.as_view(), name='vivero_create'),
    path('vivero/<str:pk>/update/', views.ViveroUpdate.as_view(), name='vivero_update'),
    path('vivero/<str:pk>/delete/', views.ViveroDelete.as_view(), name='vivero_delete'),
    path('vivero/<str:pk>/detail/', views.ViveroDetail.as_view(), name='vivero_detail'),
    #Productor
    path('productor/', views.ProductorView.as_view(), name='productor_list'),
    path('productor/create/', views.ProductorCreate.as_view(), name='productor_create'),
    path('productor/<str:pk>/update/', views.ProductorUpdate.as_view(), name='productor_update'),
    path('productor/<str:pk>/delete/', views.ProductorDelete.as_view(), name='productor_delete'),
    path('productor/<str:pk>/detail/', views.ProductorDetail.as_view(), name='productor_detail'),
    #Producto Control
    path('procontrol/', views.ProductoControlView.as_view(), name='productocontrol_list'),
    path('procontrol/create/', views.ProductoControlCreate.as_view(), name='productocontrol_create'),
    path('procontrol/<str:pk>/update/', views.ProductoControlUpdate.as_view(), name='productocontrol_update'),
    path('procontrol/<str:pk>/delete/', views.ProductoControlDelete.as_view(), name='productocontrol_delete'),
    #Hongo
    path('procontrolho/', views.ProductoControlHongoView.as_view(), name='productocontrolhongo_list'),
    path('procontrolho/create/', views.ProductoControlHongoCreate.as_view(), name='productocontrolhongo_create'),
    path('procontrolho/<str:pk>/update/', views.ProductoControlHongoUpdate.as_view(), name='productocontrolhongo_update'),
    path('procontrolho/<str:pk>/delete/', views.ProductoControlHongoDelete.as_view(), name='productocontrolhongo_delete'),
    path('procontrolho/<str:pk>/detail/', views.ProductoControlHongoDetail.as_view(), name='productocontrolhongo_detail'),
    #Plaga
    path('procontrolpl/', views.ProductoControlPlagaView.as_view(), name='productocontrolplaga_list'),
    path('procontrolpl/create/', views.ProductoControlPlagaCreate.as_view(), name='productocontrolplaga_create'),
    path('procontrolpl/<str:pk>/update/', views.ProductoControlPlagaUpdate.as_view(), name='productocontrolplaga_update'),
    path('procontrolpl/<str:pk>/delete/', views.ProductoControlPlagaDelete.as_view(), name='productocontrolplaga_delete'),
    path('procontrolpl/<str:pk>/detail/', views.ProductoControlPlagaDetail.as_view(), name='productocontrolplaga_detail'),
    #Fertilizante
    path('procontrolfe/', views.ProductoControlFertilizanteView.as_view(), name='productocontrolfertilizante_list'),
    path('procontrolfe/create/', views.ProductoControlFertilizanteCreate.as_view(), name='productocontrolfertilizante_create'),
    path('procontrolfe/<str:pk>/update/', views.ProductoControlFertilizanteUpdate.as_view(), name='productocontrolfertilizante_update'),
    path('procontrolfe/<str:pk>/delete/', views.ProductoControlFertilizanteDelete.as_view(), name='productocontrolfertilizante_delete'),
    path('procontrolfe/<str:pk>/detail/', views.ProductoControlFertilizanteDetail.as_view(), name='productocontrolfertilizante_detail'),
    #Labor
    path('lab/', views.LaborView.as_view(), name='labor_list'),
    path('lab/create/', views.LaborCreate.as_view(), name='labor_create'),
    path('lab/<str:pk>/update/', views.LaborUpdate.as_view(), name='labor_update'),
    path('lab/<str:pk>/delete/', views.LaborDelete.as_view(), name='labor_delete'),
    path('lab/<str:pk>/detail/', views.LaborDetail.as_view(), name='labor_detail'),

    #path('empleado/create/', views.EmpleadoCreate.as_view(), name='empleado_create'),
    path('empl/create/', views.SignUp.as_view(), name="empleado_create")
]
