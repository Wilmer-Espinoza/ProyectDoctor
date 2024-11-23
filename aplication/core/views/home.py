from django.views.generic import TemplateView
from aplication.core.models import Paciente
from aplication.attention.models import CitaMedica, Atencion
from datetime import date

class HomeTemplateView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Basic context data
        context["title"] = "MediCore"
        context["title1"] = "Sistema Medico"
        context["title2"] = "Sistema Medico"
        
        # Patient statistics
        context["can_paci"] = Paciente.cantidad_pacientes()
        context["ultimo_paciente"] = Paciente.objects.order_by('-id').first()
        
        # Appointments data
        context["proximas_citas"] = CitaMedica.objects.filter(
            fecha=date.today(),
            estado='P'  # Pending appointments
        ).order_by('hora_cita')
        
        context["ultima_cita_completada"] = CitaMedica.objects.filter(
            estado='R'  # Completed appointments
        ).order_by('-fecha', '-hora_cita').first()
        
        context["ultima_cita"] = CitaMedica.objects.order_by(
            '-fecha', '-hora_cita'
        ).first()
        
        # Attention data
        context["total_atenciones"] = Atencion.objects.count()
        context["ultima_atencion"] = Atencion.objects.order_by('-fecha_atencion').first()
        
        return context