from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Doctor

class DoctorCreateView(LoginRequiredMixin, CreateView):
    model = Doctor
    fields = ['foto', 'cedula', 'nombres', 'fecha_nacimiento', 'sexo', 'codigoUnicoDoctor', 'apellidos', 'direccion', 'telefonos', 'email', 'latitud', 'longitud', 'horario_atencion', 'duracion_cita', 'activo', 'especialidad', 'curriculum', 'firmaDigital', 'imagen_receta']
    template_name = 'core/Doctor/doctor_form.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Asigna el usuario autenticado
        return super().form_valid(form)
