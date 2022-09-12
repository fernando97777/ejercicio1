
from django.contrib import admin
from django.urls import path
from miapp.views import PrimeraVista,Vista2

urlpatterns = [
    path("admin/", admin.site.urls),
    path("vistauno/",PrimeraVista.as_view(),name='vista_uno'),
    path("vistados/",Vista2,name="vista_dos")

]
