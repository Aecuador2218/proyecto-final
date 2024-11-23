from aplication.core.models import TipoSangre
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView,DetailView

class TipoSangrelistview(ListView):
    model = TipoSangre
    template_name = 'core/tiposangre/list.html'
    context_object_name='tiposangre1'
    
   
    
class TipoSangreDetail(DetailView):
    model= TipoSangre
    template_name='core/tiposangre/detalle.html'
    context_object_name='TipoSangre'

class TipoSangreCreateView(CreateView):
    model = TipoSangre
    fields = ['tipo','descripcion']
    template_name = 'core/tiposangre/form.html'
    success_url = reverse_lazy('core:tipodesangre_list')



class TipoSangreUpdateView(UpdateView):
    model = TipoSangre
    fields = ['tipo','descripcion']
    template_name = 'core/tiposangre/editar.html'
    success_url = reverse_lazy('core:tipodesangre_list')



class TipoSangreDeleteView(DeleteView):
    model = TipoSangre
    template_name = 'core/tiposangre/eliminar.html'
    success_url = reverse_lazy('core:tipodesangre_list')
                           