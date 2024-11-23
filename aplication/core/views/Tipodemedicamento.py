from aplication.core.models import TipoMedicamento, MarcaMedicamento
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView,DetailView

class TipoMedicamentoListView(ListView):
    model = TipoMedicamento
    template_name = 'core/tipodemedicamento/list3.html'
    context_object_name='tipomedicamento1'

class TipoMedicamentoDetailView(DetailView):
    model= TipoMedicamento
    template_name='core/tipodemedicamento/detalle3.html'
    context_object_name='tipomedicamento'


class TipoMedicamentoCreateView(CreateView):
    model = TipoMedicamento
    fields = ['nombre','descripcion','activo']
    template_name = 'core/tipodemedicamento/form3.html'
    success_url = reverse_lazy('core:listTipoMedicamento')
    context_object_name='tipomedicamento'

class TipoMedicamentoDeleteView(DeleteView):
    model = TipoMedicamento
    template_name = 'core/tipodemedicamento/eliminar3.html'
    success_url = reverse_lazy('core:listTipoMedicamento')
    context_object_name='tipomedicamento'


class TipoMedicamentoUpdateView(UpdateView):
 model = TipoMedicamento
 fields = ['nombre','descripcion','activo']
 template_name = 'core/tipodemedicamento/editar3.html'
 success_url = reverse_lazy('core:listTipoMedicamento')
 context_object_name='tipomedicamento'



#MARCA DE MEDICAMENTO
class MarcaMedicamentoListView(ListView):
    model = MarcaMedicamento
    template_name = 'core/tipodemedicamento/listmarca.html'
    context_object_name='marca1'

class MarcaMedicamentoDetailView(DetailView):
    model= MarcaMedicamento
    template_name='core/tipodemedicamento/detallemarca.html'
    context_object_name='marca'

class MarcaMedicamentoCreateView(CreateView):
    model = MarcaMedicamento
    fields = ['nombre','descripcion','activo']
    template_name = 'core/tipodemedicamento/formmarca.html'
    success_url = reverse_lazy('core:listMarca')
    context_object_name='marca'

class MarcaMedicamentoDeleteView(DeleteView):
    model = MarcaMedicamento
    template_name = 'core/tipodemedicamento/eliminarmarca.html'
    success_url = reverse_lazy('core:listMarca')
    context_object_name='marca'


class MarcaMedicamentoUpdateView(UpdateView):
 model = MarcaMedicamento
 fields = ['nombre','descripcion','activo']
 template_name = 'core/tipodemedicamento/editarmarca.html'
 success_url = reverse_lazy('core:listMarca')
 context_object_name='marca'
