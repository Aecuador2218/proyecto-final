from django.urls import reverse_lazy
from aplication.core.forms.Doctor import DoctorForm
from aplication.core.models import Doctor
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit



class DoctorListView(ListView):
    template_name = "core/Doctor/list.html"
    model = Doctor
    context_object_name = 'doctor1'
    paginate_by = 2
    
    def get_queryset(self):
        query = Q()
        q1 = self.request.GET.get('q')
        sex = self.request.GET.get('sex')
        if q1 is not None: 
            query.add(Q(nombres__icontains=q1), Q.OR) 
            query.add(Q(apellidos__icontains=q1), Q.OR) 
            query.add(Q(cedula__icontains=q1), Q.OR) 
        if sex in ["M", "F"]:
            query.add(Q(sexo__icontains=sex), Q.AND)
        return self.model.objects.filter(query).order_by('apellidos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = "Consulta de Doctores"
        return context
    

class DoctorCreateView(CreateView):
    model = Doctor
    template_name = 'core/Doctor/form.html'
    
    form_class = DoctorForm
    success_url = reverse_lazy('core:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Ingresar información del Doctor'
        context['grabar'] = 'Grabar Doctor'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        doctor = self.object  # Changed patient to doctor for clarity
        save_audit(self.request, doctor, action='A')
        messages.success(self.request, f"Éxito al crear al Doctor {doctor.nombre_completo}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    

class DoctorUpdateView(UpdateView):
    model = Doctor
    template_name = 'core/Doctor/form.html'
    form_class = DoctorForm
    success_url = reverse_lazy('core:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['title1'] = 'Modificar información del Doctor'
        context['grabar'] = 'Actualizar Doctor'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        doctor = self.object  # Changed patient to doctor for clarity
        save_audit(self.request, doctor, action='M')
        messages.success(self.request, f"Éxito al Modificar el Doctor {doctor.nombre_completo}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al Modificar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    

class DoctorDeleteView(DeleteView):
    model = Doctor
    success_url = reverse_lazy('core:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "SaludSync"
        context['grabar'] = 'Eliminar al doctor'
        context['description'] = f"¿Desea eliminar al doctor: {self.object.nombre_completo}?"  # Usar nombre completo
        context['back_url'] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Borrado lógico en lugar de eliminación física
        self.object.activo = False  # O usa `self.object.deleted = True` si tienes un campo deleted
        self.object.save()
        success_message = f"Éxito al eliminar lógicamente al doctor {self.object.nombre_completo}."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)

class DoctorDetailView(DetailView):
    model = Doctor

    def get(self, request, *args, **kwargs):
        doctor = self.get_object()
        data = {
            "id": doctor.id,
            "nombres": doctor.nombres,
            "apellidos": doctor.apellidos,
            "foto": doctor.get_image(),
            "fecha_nac": doctor.fecha_nacimiento,
            "dni": doctor.cedula,
            "telefonos": doctor.telefonos,
            "email": doctor.email,
            "direccion": doctor.direccion,
            "especialidad": [esp.nombre for esp in doctor.especialidad.all()],
        }
        return JsonResponse(data)

 