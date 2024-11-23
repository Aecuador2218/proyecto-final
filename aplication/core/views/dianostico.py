from aplication.core.models import Diagnostico
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView,DetailView

class DiagnosticoListView(ListView):
    model = Diagnostico
    template_name = 'core/diagnostico/list1.html'
    context_object_name = 'diag1'

class DiagnosticoDetailView(DetailView):
    model = Diagnostico
    template_name = 'core/diagnostico/detalle1.html'
    context_object_name = 'diag'

class DiagnosticoCreateView(CreateView):
    model = Diagnostico
    fields = ['codigo','descripcion','datos_adicionales','activo',]
    template_name = 'core/diagnostico/form1.html'
    success_url = reverse_lazy('core:listardiagnostico')
    context_object_name='diag'

class DiagnosticoDeleteView(DeleteView):
    model = Diagnostico
    template_name = 'core/tipodemedicamento/eliminar3.html'
    success_url = reverse_lazy('core:listardiagnostico')
    context_object_name='diag'


class DiagnosticoUpdateView(UpdateView):
 model =Diagnostico
 fields = ['codigo','descripcion','datos_adicionales','activo',]  
 template_name = 'core/diagnostico/editar1.html'
 success_url = reverse_lazy('core:listardiagnostico')
 context_object_name='diag'
