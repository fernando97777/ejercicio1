from django.shortcuts import render
from django.views.generic import ListView
from miapp.models import Profile


#vista uno
#vista basada en clases
class PrimeraVista(ListView):
    model = Profile
    template_name = "vistauno.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado desde el admin'
        return context


#vista dos
#vista basada en funciones
def Vista2(request):
    return render(request,'vistados.html')