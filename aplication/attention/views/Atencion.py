from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from aplication.attention.models import Atencion
class AtencionListView(ListView):
    model = Atencion
    template_name = 'core/Atencion/atencion_list.html'
    context_object_name = 'atenciones'


class AtencionDetailView(DetailView):
    model = Atencion
    template_name = 'core/Atencion/atencion_detail.html'
    context_object_name = 'atencion'


class AtencionCreateView(CreateView):
    model = Atencion
    fields = ['paciente', 'diagnostico', 'motivo_consulta', 'tratamiento', 'comentario']
    template_name = 'core/Atencion/atencion_form.html'
    success_url = reverse_lazy('core:atencion_list')


class AtencionUpdateView(UpdateView):
    model = Atencion
    fields = ['paciente', 'diagnostico', 'motivo_consulta', 'tratamiento', 'comentario']
    template_name = 'core/Atencion/atencion_form.html'
    success_url = reverse_lazy('core:atencion_list')


class AtencionDeleteView(DeleteView):
    model = Atencion
    template_name = 'core/Atencion/atencion_confirm_delete.html'
    success_url = reverse_lazy('core:atencion_list')
