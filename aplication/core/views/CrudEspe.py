from aplication.core.models import Especialidad # noqa
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView,DetailView

class EspecialidadListView(ListView):
    model = Especialidad
    template_name = 'core/CrudEspe/list1.html'
    context_object_name='espe1'

class EspecialidadDetailView(DetailView):
    model = Especialidad
    template_name = 'core/CrudEspe/detalle1.html'
    context_object_name='espe'

class EspecialidadCreateView(CreateView):
    model = Especialidad
    template_name = 'core/CrudEspe/form1.html'
    fields = ['nombre','descripcion','activo']
    success_url = reverse_lazy('core:listarespe')

class EspecialidadUpdateView(UpdateView):
    model = Especialidad
    template_name = 'core/CrudEspe/editar1.html'
    fields = ['nombre','descripcion','activo']
    success_url = reverse_lazy('core:listarespe')

class EspecialidadDeleteView(DeleteView):
    model = Especialidad
    template_name = 'core/CrudEspe/eliminar1.html'
    success_url = reverse_lazy('core:listarespe')
    context_object_name='espe'
