from django.forms import ModelForm, ValidationError
from django import forms
from django.forms.widgets import TextInput, EmailInput, DateInput, FileInput, Select, CheckboxInput  # Importación de widgets
from aplication.core.models import Paciente

# Definición de la clase PatientForm que hereda de ModelForm
class PatientForm(ModelForm):
    class Meta:
        model = Paciente
        # Campos que se muestran en el formulario
        fields = [
            "nombres", "apellidos", "cedula", "fecha_nacimiento", "telefono", 
            "email", "sexo", "estado_civil", "direccion", "latitud", "longitud", 
            "tipo_sangre", "foto", "alergias", "enfermedades_cronicas", 
            "medicacion_actual", "cirugias_previas", "antecedentes_personales", 
            "antecedentes_familiares", "activo"
        ]

        # Personalización de widgets
        widgets = {
            "nombres": TextInput(attrs={"placeholder": "Ingrese nombres", "class": "form-control"}),
            "apellidos": TextInput(attrs={"placeholder": "Ingrese apellidos", "class": "form-control"}),
            "cedula": TextInput(attrs={"placeholder": "Ingrese cédula", "class": "form-control"}),
            "fecha_nacimiento": DateInput(attrs={"type": "date", "class": "form-control"}),
            "telefono": TextInput(attrs={"placeholder": "Ingrese teléfono", "class": "form-control"}),
            "email": EmailInput(attrs={"placeholder": "Ingrese correo electrónico", "class": "form-control"}),
            "sexo": Select(attrs={"class": "form-control"}),
            "estado_civil": Select(attrs={"class": "form-control"}),
            "direccion": TextInput(attrs={"placeholder": "Ingrese dirección", "class": "form-control"}),
            "latitud": TextInput(attrs={"placeholder": "Coordenada: latitud", "class": "form-control"}),
            "longitud": TextInput(attrs={"placeholder": "Coordenada: longitud", "class": "form-control"}),
            "tipo_sangre": Select(
                choices=[("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"), 
                         ("O+", "O+"), ("O-", "O-"), ("AB+", "AB+"), ("AB-", "AB-")],
                attrs={"class": "form-control"}
            ),
            "foto": FileInput(attrs={"class": "form-control"}),
            "alergias": TextInput(attrs={"placeholder": "Ingrese alergias", "class": "form-control"}),
            "enfermedades_cronicas": TextInput(attrs={"placeholder": "Ingrese enfermedades crónicas", "class": "form-control"}),
            "medicacion_actual": TextInput(attrs={"placeholder": "Ingrese medicación actual", "class": "form-control"}),
            "cirugias_previas": TextInput(attrs={"placeholder": "Ingrese cirugías previas", "class": "form-control"}),
            "antecedentes_personales": TextInput(attrs={"placeholder": "Ingrese antecedentes personales", "class": "form-control"}),
            "antecedentes_familiares": TextInput(attrs={"placeholder": "Ingrese antecedentes familiares", "class": "form-control"}),
            "activo": CheckboxInput(attrs={"class": "form-check-input"}),
        }

    # Validación personalizada para el campo "tipo_sangre"
    def clean_tipo_sangre(self):
        tipo_sangre = self.cleaned_data.get("tipo_sangre")
        valid_types = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

        if tipo_sangre not in valid_types:
            raise ValidationError("Tipo de sangre inválido. Use formatos como: O+, A-, AB+.")
        
        return tipo_sangre

    # Validación personalizada para el campo "nombres"
    def clean_nombres(self):
        nombres = self.cleaned_data.get("nombres")
        if not nombres or len(nombres) < 2:
            raise ValidationError("El nombre debe tener al menos 2 caracteres.")
        return nombres.upper()

    # Validación personalizada para el campo "apellidos"
    def clean_apellidos(self):
        apellidos = self.cleaned_data.get("apellidos")
        if not apellidos or len(apellidos) < 1:
            raise ValidationError("El apellido debe tener al menos 1 carácter.")
        return apellidos.upper()
