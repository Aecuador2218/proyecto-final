from django.urls import path
from aplication.core.views.home import HomeTemplateView
from aplication.core.views.patient import PatientCreateView, PatientDeleteView, PatientDetailView, PatientListView, PatientUpdateView
from aplication.core.views.crudtiposangre import TipoSangrelistview,TipoSangreCreateView,TipoSangreUpdateView,TipoSangreDetail,TipoSangreDeleteView
from aplication.core.views.CrudEspe import EspecialidadListView, EspecialidadCreateView, EspecialidadUpdateView, EspecialidadDetailView, EspecialidadDeleteView
from aplication.core.views.CrudCargo import CargoListView, CargoCreateView, CargoUpdateView, CargoDetailView, CargoDeleteView
from aplication.core.views.Doctores import DoctorCreateView, DoctorDeleteView, DoctorDetailView, DoctorListView, DoctorUpdateView
from aplication.core.views.empleado import EmpleadoCreateView, EmpleadoDeleteView, EmpleadoListView, EmpleadoDetailView, EmpleadoUpdateView
from aplication.core.views.Tipodemedicamento import TipoMedicamentoListView, TipoMedicamentoDetailView, TipoMedicamentoCreateView, TipoMedicamentoDeleteView, TipoMedicamentoUpdateView,MarcaMedicamentoCreateView,MarcaMedicamentoDeleteView,MarcaMedicamentoDetailView,MarcaMedicamentoListView,MarcaMedicamentoUpdateView
from aplication.core.views.medicamento import MedicamentoListView,MedicamentoCreateView,MedicamentoUpdateView,MedicamentoDeleteView,MedicamentoDetailView
from aplication.core.views.dianostico import DiagnosticoCreateView,DiagnosticoDeleteView,DiagnosticoDetailView,DiagnosticoListView,DiagnosticoUpdateView
from aplication.core.views. auditroria import AuditUserListView, AuditUserDetailView
from aplication.core.views.DashboardView import DashboardView,DashboardAtencionView
from aplication.attention.views.HorarioAtencion import HorarioAtencionListView, HorarioAtencionDetailView, HorarioAtencionCreateView, HorarioAtencionUpdateView
from aplication.attention.views.CitaMedica import CitaMedicaCreateView,CitaMedicaDeleteView,CitaMedicaDetailView, CitaMedicaListView,CitaMedicaUpdateView
from aplication.attention.views.Atencion import AtencionListView,AtencionDetailView, AtencionCreateView, AtencionUpdateView, AtencionDeleteView
from aplication.attention.views.Detalle import DetalleAtencionCreateView,DetalleAtencionDeleteView,DetalleAtencionDetailView,DetalleAtencionUpdateView,DetalleAtencionListView
from aplication.attention.views.Servicios import ServiciosAdicionalesCreateView,ServiciosAdicionalesListView,ServiciosAdicionalesUpdateView,ServiciosAdicionalesDeleteView
from aplication.attention.views.CostoAtencion import CostosAtencionCreateView,CostosAtencionListView,CostosAtencionUpdateView,CostosAtencionDeleteView
from aplication.attention.views.CostoAtencionDetalle import (
    CostoAtencionDetalleListView,
    CostoAtencionDetalleCreateView,
    CostoAtencionDetalleUpdateView,
    CostoAtencionDetalleDeleteView,
)
app_name='core' # define un espacio de nombre para la aplicacio
urlpatterns = [
  path('', HomeTemplateView.as_view(),name='home'),
  path('patient_list/',PatientListView.as_view() ,name="patient_list"),
  path('patient_create/',PatientCreateView.as_view(),name="patient_create"),
  path('patien_update/<int:pk>/', PatientUpdateView.as_view(),name='patient_update'),
  path('patient_delete/<int:pk>/', PatientDeleteView.as_view(),name='patient_delete'),
  path('patient_detail/<int:pk>/', PatientDetailView.as_view(),name='patient_detail'),
  #RUTA TIPO DE SANGRE 
  path('tiposangre/', TipoSangrelistview.as_view(), name='tipodesangre_list'),
  path('tipodesangrecrear/', TipoSangreCreateView.as_view(), name='tipodesangre_crear'),
  path('<int:pk>', TipoSangreDetail.as_view(), name='detalle'),
  path('tiposangre/<int:pk>/editar/', TipoSangreUpdateView.as_view(), name='editar'),
  path('tiposangre/<int:pk>/eliminar/', TipoSangreDeleteView.as_view(), name='eliminar'),
  #RUTA Especialidad
  path('espcialidad/', EspecialidadListView.as_view(), name='listarespe'),
  path('espcialidadcrear/',EspecialidadCreateView.as_view(), name='crearespe'),
  path('<int:pk>', EspecialidadDetailView.as_view(), name='detalleespe'),
  path('espcialidadedit/<int:pk>/editar/', EspecialidadUpdateView.as_view(), name='editarespe'),
  path('espcialidaddelete/<int:pk>/eliminar/', EspecialidadDeleteView.as_view(), name='eliminarespe'),
  #RUTA Especialidad
  path('Cargo/', CargoListView.as_view(), name='listarcargo'),
  path('Cargocrear/', CargoCreateView.as_view(), name='crearcargo'),
  path('<int:pk>', CargoDetailView.as_view(), name='detallecargo'),
  path('Cargoedit/<int:pk>/editar/', CargoUpdateView.as_view(), name='editarcargo'),
  path('Cargodelete/<int:pk>/eliminar/', CargoDeleteView.as_view(), name='eliminarcargo'), 
  #Ruta para doctor
  path('Doctor_list/',DoctorListView.as_view() ,name="doctor_list"),
  path('Doctor_create/',DoctorCreateView.as_view(),name="doctor_create"),
  path('Doctor_update/<int:pk>/', DoctorUpdateView.as_view(),name='doctor_update'),
  path('doctor_delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),
  path('doctor_detail/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
  #Ruta Empleado
  path('empleado_list/',EmpleadoListView.as_view() ,name="empleado_list"),
  path('empleado_create/', EmpleadoCreateView.as_view(),name="empleado_create"),
  path('empleado_update/<int:pk>/', EmpleadoUpdateView.as_view(),name='empleado_update'),
  path('empleado_delete/<int:pk>/', EmpleadoDeleteView.as_view(),name='empleado_delete'),
  path('empleado_detail/<int:pk>/', EmpleadoDetailView.as_view(),name='empleado_detail'), 
  # Ruta tipo de medicamento 
  path('tipomedicamento_list/',TipoMedicamentoListView.as_view() ,name="listTipoMedicamento"),
  path('tipomedicamentocrear/', TipoMedicamentoCreateView.as_view(), name='crearTipoMedicamento'),
  path('<int:pk>',TipoMedicamentoDetailView.as_view(), name='detalleTipoMedicamento'),
  path('tipomedicamentoedit/<int:pk>/editar/', TipoMedicamentoUpdateView.as_view(), name='editarTipoMedicamento'),
  path('tipomedicamentodelete/<int:pk>/eliminar/', TipoMedicamentoDeleteView.as_view(), name='eliminarTipoMedicamento'),
  # Marca de marca medicamento
  path('marcamedicamento_list/',MarcaMedicamentoListView.as_view() ,name="listMarca"),
  path('marcamedicamentocrear/', MarcaMedicamentoCreateView.as_view(), name='crearMarca'),
  path('<int:pk>',MarcaMedicamentoDetailView.as_view(), name='detalleMarca'),
  path('marcamedicamentoedit/<int:pk>/editar/', MarcaMedicamentoUpdateView.as_view(), name='editarMarca'),
  path('marcamedicamentodelete/<int:pk>/eliminar/', MarcaMedicamentoDeleteView.as_view(), name='eliminarMarca'),
  #Url de medicamento
  path('medicamento_list/', MedicamentoListView.as_view(), name="medicamento_list"),
  path('medicamento_create/', MedicamentoCreateView.as_view(), name="medicamento_create"),
  path('medicamento_update/<int:pk>/', MedicamentoUpdateView.as_view(), name='medicamento_update'),
  path('medicamento_delete/<int:pk>/', MedicamentoDeleteView.as_view(), name='medicamento_delete'),
  path('medicamento_detail/<int:pk>/', MedicamentoDetailView.as_view(), name='medicamento_detail'),
  #url de diagnostico
  path('diagnostico/',DiagnosticoListView.as_view(), name='listardiagnostico'),
  path('diagnosticocrear/', DiagnosticoCreateView.as_view(), name='creardiagnostico'),
  path('<int:pk>',DiagnosticoDetailView.as_view(), name='detallediagnostico'),
  path('diagnosticodit/<int:pk>/editar/',DiagnosticoUpdateView.as_view(), name='editardiagnostico'),
  path('diagnosticodelete/<int:pk>/eliminar/',DiagnosticoDeleteView.as_view(), name='eliminardiagnostico'),
  #Ruta auditoria
  path('auditoria/', AuditUserListView.as_view(), name='lista_auditoria'),
  path('auditoriaver/<int:pk>/', AuditUserDetailView.as_view(), name='detalle_auditoria'),
  #Ruta de Horarios
  path('horarios/', HorarioAtencionListView.as_view(), name='horario_list'),
  path('<int:pk>/', HorarioAtencionDetailView.as_view(), name='horario_detail'),
  path('horarios2/nuevo/', HorarioAtencionCreateView.as_view(), name='horario_create'),
  path('horarios3/<int:pk>/editar/', HorarioAtencionUpdateView.as_view(), name='horario_edit'),
  #ruta de citasmedicas
  path('citas/', CitaMedicaListView.as_view(), name='cita_list'),
  path('<int:pk>/', CitaMedicaDetailView.as_view(), name='cita_detail'),
  path('citas2/nueva/', CitaMedicaCreateView.as_view(), name='cita_create'),
  path('citas3/<int:pk>/editar/', CitaMedicaUpdateView.as_view(), name='cita_edit'),
  path('citas4/<int:pk>/eliminar/', CitaMedicaDeleteView.as_view(), name='cita_delete'),
  #ruta atencion
  path('atenciones/', AtencionListView.as_view(), name='atencion_list'),
  path('atencion1/<int:pk>/', AtencionDetailView.as_view(), name='atencion_detail'),
  path('atencion2/nueva/', AtencionCreateView.as_view(), name='atencion_create'),
  path('atencion3/<int:pk>/editar/', AtencionUpdateView.as_view(), name='atencion_edit'),
  path('atencion4/<int:pk>/eliminar/', AtencionDeleteView.as_view(), name='atencion_delete'),
  #ruta de detalle atencion
  path('detalle_atencion/', DetalleAtencionListView.as_view(), name='detalle_atencion_list'),
  path('detalle_atencion/<int:pk>/', DetalleAtencionDetailView.as_view(), name='detalle_atencion_detail'),
  path('detalle_atencion/nuevo/', DetalleAtencionCreateView.as_view(), name='detalle_atencion_create'),
  path('detalle_atencion/<int:pk>/editar/', DetalleAtencionUpdateView.as_view(), name='detalle_atencion_edit'),
  path('detalle_atencion/<int:pk>/eliminar/', DetalleAtencionDeleteView.as_view(), name='detalle_atencion_delete'),
  #Ruta de Servisios adicionales
  path('servicios/', ServiciosAdicionalesListView.as_view(), name='servicios_list'),
  path('servicios2/nuevo/', ServiciosAdicionalesCreateView.as_view(), name='servicios_create'),
  path('servicios3/editar/<int:pk>/', ServiciosAdicionalesUpdateView.as_view(), name='servicios_edit'),
  path('servicios4/eliminar/<int:pk>/', ServiciosAdicionalesDeleteView.as_view(), name='servicios_eliminar'),
  ##ruta de las opciones
  path('costos-atencion/', CostosAtencionListView.as_view(), name='CostosAtencion_list'),
  path('costos-atencion1/nuevo/', CostosAtencionCreateView.as_view(), name='CostosAtencion_create'),
  path('costos-atencion2/<int:pk>/editar/', CostosAtencionUpdateView.as_view(), name='CostosAtencion_edit'),
  path('costos-atencion3/<int:pk>/eliminar/', CostosAtencionDeleteView.as_view(), name='CostosAtencion_eliminar'),
  # Ruta tipo de medicamento 
  path('tipomedicamento_list/',TipoMedicamentoListView.as_view() ,name="listTipoMedicamento"),
  path('tipomedicamentocrear/', TipoMedicamentoCreateView.as_view(), name='crearTipoMedicamento'),
  path('<int:pk>',TipoMedicamentoDetailView.as_view(), name='detalleTipoMedicamento'),
  path('tipomedicamentoedit/<int:pk>/editar/', TipoMedicamentoUpdateView.as_view(), name='editarTipoMedicamento'),
  path('tipomedicamentodelete/<int:pk>/eliminar/', TipoMedicamentoDeleteView.as_view(), name='eliminarTipoMedicamento'),
  # Marca de marca medicamento
  path('marcamedicamento_list/',MarcaMedicamentoListView.as_view() ,name="listMarca"),
  path('marcamedicamentocrear/', MarcaMedicamentoCreateView.as_view(), name='crearMarca'),
  path('<int:pk>',MarcaMedicamentoDetailView.as_view(), name='detalleMarca'),
  path('marcamedicamentoedit/<int:pk>/editar/', MarcaMedicamentoUpdateView.as_view(), name='editarMarca'),
  path('marcamedicamentodelete/<int:pk>/eliminar/', MarcaMedicamentoDeleteView.as_view(), name='eliminarMarca'),
  #Ruta auditoria
  path('auditoria/', AuditUserListView.as_view(), name='lista_auditoria'),
  path('auditoriaver/<int:pk>/', AuditUserDetailView.as_view(), name='detalle_auditoria'),
  path('costos-atencion/', CostosAtencionListView.as_view(), name='CostosAtencion_list'),
  #Costos de Atencion
  path('costos-atencion/', CostosAtencionListView.as_view(), name='CostosAtencion_list'),
  path('costos-atencion1/nuevo/', CostosAtencionCreateView.as_view(), name='CostosAtencion_create'),
  path('costos-atencion2/<int:pk>/editar/', CostosAtencionUpdateView.as_view(), name='CostosAtencion_edit'),
  path('costos-atencion3/<int:pk>/eliminar/', CostosAtencionDeleteView.as_view(), name='CostosAtencion_eliminar'),
  #Detalle de Atencion
  path('detalleatencion1', CostoAtencionDetalleListView.as_view(), name='costos_atencion_detalle_list'),
  path('nuevo/', CostoAtencionDetalleCreateView.as_view(), name='costos_atencion_detalle_create'),
  path('<int:pk>/editar/', CostoAtencionDetalleUpdateView.as_view(), name='costos_atencion_detalle_update'),

  #Ruta dashboard
  path('dashboard/', DashboardView.as_view(), name='dashboard'),
  path('dashboardAtencion/', DashboardAtencionView.as_view(), name='dashboardAtencion'),
]
