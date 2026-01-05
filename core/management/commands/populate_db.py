from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Laboratorio, Equipamento, Reserva
from django.utils import timezone
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados fictícios para teste'

    def handle(self, *args, **kwargs):
        self.stdout.write('Iniciando população do banco de dados...')

        usuarios_nomes = ['Dra. Ana Silva', 'Prof. Carlos Santos', 'Pesquisador Pedro']
        usuarios_objs = []
        for nome in usuarios_nomes:
            username = nome.lower().replace(' ', '').replace('.', '')
            user, created = User.objects.get_or_create(username=username, defaults={'email': f'{username}@lab.edu'})
            if created:
                user.set_password('senha123')
                user.save()
            usuarios_objs.append(user)
        self.stdout.write(f'{len(usuarios_objs)} usuários verificados/criados.')

        labs_data = [
            ('Laboratório de Química Orgânica', 'Bloco A, Sala 101'),
            ('Laboratório de Física Experimental', 'Bloco B, Sala 204'),
            ('Centro de Genética', 'Bloco C, 3º Andar'),
            ('Sala de Microscopia', 'Bloco A, Térreo'),
        ]
        labs_objs = []
        for nome, desc in labs_data:
            lab, _ = Laboratorio.objects.get_or_create(nome=nome, defaults={'descricao': desc})
            labs_objs.append(lab)
        self.stdout.write(f'{len(labs_objs)} laboratórios verificados/criados.')

        equipamentos_nomes = [
            'Espectrofotômetro UV-Vis', 'Centrífuga Refrigerada', 'Microscópio Eletrônico',
            'Balança de Precisão', 'Agitador Magnético', 'Estufa de Secagem',
            'Autoclave Vertical', 'Capela de Exaustão', 'pHmetro Digital'
        ]
        
        status_choices = ['ativo', 'ativo', 'ativo', 'manutencao', 'inativo'] # Peso maior para ativo

        for nome_eq in equipamentos_nomes:
            Equipamento.objects.get_or_create(
                nome=nome_eq,
                laboratorio=random.choice(labs_objs),
                defaults={
                    'status': random.choice(status_choices),
                    'ultima_calibragem': timezone.now() - timedelta(days=random.randint(1, 365))
                }
            )
        self.stdout.write('Equipamentos populados.')

        agora = timezone.now()
        
        for i in range(6): 
            data_base = agora + timedelta(days=i)
            for _ in range(2):
                hora_inicio = data_base.replace(hour=random.randint(8, 16), minute=0, second=0, microsecond=0)
                hora_fim = hora_inicio + timedelta(hours=2)
                
                lab_random = random.choice(labs_objs)
                user_random = random.choice(usuarios_objs)
                
                if not Reserva.objects.filter(laboratorio=lab_random, data_inicio=hora_inicio).exists():
                    Reserva.objects.create(
                        usuario=user_random,
                        laboratorio=lab_random,
                        data_inicio=hora_inicio,
                        data_fim=hora_fim,
                        descricao="Aula Prática e Pesquisa"
                    )

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))