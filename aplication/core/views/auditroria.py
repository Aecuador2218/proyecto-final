from aplication.core.models import AuditUser
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView

class AuditUserListView(ListView):
    model = AuditUser
    template_name = 'core/audituser/lista_auditoria.html'
    context_object_name = 'auditorias'
    ordering = ['-fecha', '-hora']  # Ordenar por fecha y hora

class AuditUserDetailView(DetailView):
    model = AuditUser
    template_name = 'core/audituser/detalle_auditoria.html'
    context_object_name = 'auditoria'