from django.urls import reverse_lazy
from aplication.core.forms.medicamento import MedicamentoForm
from aplication.core.models import Medicamento
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit


class MedicamentoListView(ListView):
    template_name = "core/Medicamento/list.html"
    model = Medicamento
    context_object_name = 'medicamento1'
    paginate_by = 2
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = "Consulta de medicamento"
        return context
    

class MedicamentoCreateView(CreateView):
    model = Medicamento
    template_name = 'core/Medicamento/form.html'
    
    form_class = MedicamentoForm
    success_url = reverse_lazy('core:medicamento_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información de medicamento'
        context['grabar'] = 'Grabar medicamento'
        context['back_url'] = self.success_url 
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        doctor = self.object  # Changed patient to doctor for clarity
        save_audit(self.request, doctor, action='A')
        messages.success(self.request, f"Éxito al crear al medicamento {doctor.nombre}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el medicamento. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    

class MedicamentoUpdateView(UpdateView):
    model = Medicamento
    template_name = 'core/Medicamento/form.html'
    form_class = MedicamentoForm
    success_url = reverse_lazy('core:medicamento_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Modificar información del medicamento'
        context['grabar'] = 'Actualizar el medicamento'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        doctor = self.object  # Changed patient to doctor for clarity
        save_audit(self.request, doctor, action='M')
        messages.success(self.request, f"Éxito al Modificar el medicamento {doctor.nombre}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al Modificar el medicamento. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    

class MedicamentoDeleteView(DeleteView):
    model = Medicamento
    success_url = reverse_lazy('core:medicamento_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar al medicamento'
        context['description'] = f"¿Desea eliminar al medicamento: {self.object.nombre}?"  # Usar nombre completo
        context['back_url'] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Borrado lógico en lugar de eliminación física
        self.object.activo = False  # O usa `self.object.deleted = True` si tienes un campo deleted
        self.object.save()
        success_message = f"Éxito al eliminar lógicamente al medicamento {self.object.nombre}."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)

class MedicamentoDetailView(DetailView):
    model = Medicamento

    def get(self, request, *args, **kwargs):
        medicamento = self.get_object()
        data = {
            "id": medicamento.id,
            "tipo": medicamento.tipo.nombre,
            "marca": medicamento.marca_medicamento.nombre,
            "nombre": medicamento.nombre,
            "descripcion": medicamento.descripcion,
            "concentracion": medicamento.concentracion,
            "cantidad": medicamento.cantidad,
            "precio": medicamento.precio,
            "comercial": medicamento.comercial,
            "imagen": medicamento.get_image()  
        }
        return JsonResponse(data)