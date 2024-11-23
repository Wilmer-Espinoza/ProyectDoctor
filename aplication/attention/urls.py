from django.urls import path
from aplication.attention.views.certificate import CertificateListView, CertificateCreateView, CertificateUpdateView, CertificateDeleteView, CertificateDetailView, CertificatePDFView
from aplication.attention.views.medical_attention import AttentionListView, AttentionCreateView, AttentionUpdateView, AttentionDetailView   
from aplication.attention.views.quotes import QuoteListView, QuoteCreateView, QuoteUpdateView, QuoteDetailView, QuoteDeleteView
from aplication.attention.views.ScheduleAttention import ScheduleAttentionListView, ScheduleAttentionCreateView, ScheduleAttentionUpdateView, ScheduleAttentionDeleteView, ScheduleAttentionDetailView
from aplication.attention.views.serviciosAdicionales import ServiciosAdicionalesListView, ServiciosAdicionalesCreateView, ServiciosAdicionalesUpdateView, ServiciosAdicionalesDeleteView, ServiciosAdicionalesDetailView
from aplication.attention.views.clinical_record import ClinicalRecordListView, ClinicalRecordDetailView, ImprimirHistorialClinico

app_name = 'attention'  # define un espacio de nombre para la aplicacion

urlpatterns = [
  # rutas de atenciones
  path('attention_list/', AttentionListView.as_view(), name="attention_list"),
  path('attention_create/', AttentionCreateView.as_view(), name="attention_create"),
  path('attention_update/<int:pk>/', AttentionUpdateView.as_view(), name='attention_update'),
  path('attention_detail/<int:pk>/', AttentionDetailView.as_view(), name='attention_detail'),
  
  # rutas de horario de atencion
  path('schedule_attention_list/', ScheduleAttentionListView.as_view(), name="schedule_attention_list"),
  path('schedule_attention_create/', ScheduleAttentionCreateView.as_view(), name="schedule_attention_create"),
  path('schedule_attention_update/<int:pk>/', ScheduleAttentionUpdateView.as_view(), name='schedule_attention_update'),
  path('schedule_attention_delete/<int:pk>/', ScheduleAttentionDeleteView.as_view(), name='schedule_attention_delete'),
  path('schedule_attention_detail/<int:pk>/', ScheduleAttentionDetailView.as_view(), name='schedule_attention_detail'),
  
  # rutas de citas medicas
  path('quote_list/', QuoteListView.as_view(), name="quote_list"),
  path('quote_create/', QuoteCreateView.as_view(), name="quote_create"),
  path('quote_update/<int:pk>/', QuoteUpdateView.as_view(), name='quote_update'),
  path('quote_detail/<int:pk>/', QuoteDetailView.as_view(), name='quote_detail'),
  path('quote_delete/<int:pk>/', QuoteDeleteView.as_view(), name='quote_delete'),
  
  # rutas de servicios adicionales
  path('servicio_list/',ServiciosAdicionalesListView.as_view() ,name="servicio_list"),
  path('servicio_create/', ServiciosAdicionalesCreateView.as_view(),name="servicio_create"),
  path('servicio_update/<int:pk>/', ServiciosAdicionalesUpdateView.as_view(),name='servicio_update'),
  path('servicio_delete/<int:pk>/', ServiciosAdicionalesDeleteView.as_view(),name='servicio_delete'),
  path('servicio_detail/<int:pk>/', ServiciosAdicionalesDetailView.as_view(),name='servicio_detail'),
  
  # rutas de certificados
  path('certificate_list/', CertificateListView.as_view(), name="certificate_list"),
  path('certificate_create/', CertificateCreateView.as_view(), name="certificate_create"),
  path('certificate_update/<int:pk>/', CertificateUpdateView.as_view(), name='certificate_update'),
  path('certificate_delete/<int:pk>/', CertificateDeleteView.as_view(), name='certificate_delete'),
  path('certificate_detail/<int:pk>/', CertificateDetailView.as_view(), name='certificate_detail'),
  path('certificate_pdf/<int:pk>/', CertificatePDFView.as_view(), name='certificate_pdf'),
  
  # rutas de fichas clinicas
  path('clinical_record_list/', ClinicalRecordListView.as_view(), name="clinical_record_list"),
  path('clinical_record_detail/<int:pk>/', ClinicalRecordDetailView.as_view(), name='clinical_record_detail'),
  path('imprimir_historial_clinico/<int:pk>/', ImprimirHistorialClinico.as_view(), name='imprimir_historial_clinico'),
]