from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Laboratorio, Equipamento, Reserva

@login_required
def dashboard(request):
    # Estatísticas
    total_labs = Laboratorio.objects.count()
    total_equipamentos = Equipamento.objects.count()
    
    # Reservas de hoje (filtramos onde a data de inicio é maior ou igual a agora)
    reservas_futuras = Reserva.objects.filter(
        data_inicio__gte=timezone.now()
    ).order_by('data_inicio')
    
    reservas_hoje_count = reservas_futuras.filter(
        data_inicio__date=timezone.now().date()
    ).count()

    # Listas para as tabelas
    equipamentos_status = Equipamento.objects.all()[:5] # Pega os 5 primeiros
    proximas_reservas = reservas_futuras[:5]

    context = {
        'total_labs': total_labs,
        'total_equipamentos': total_equipamentos,
        'reservas_hoje_count': reservas_hoje_count,
        'equipamentos_status': equipamentos_status,
        'proximas_reservas': proximas_reservas,
    }
    
    return render(request, 'core/dashboard.html', context)